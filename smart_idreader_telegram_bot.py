# Copyright (c) 2012-2017, Smart Engines Ltd
# All rights reserved.

# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:

# * Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
# * Neither the name of the Smart Engines Ltd nor the names of its
# contributors may be used to endorse or promote products derived from this
# software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import pySmartIdEngine as se  # Smart IDReader by Smart Engines

import telepot
from telepot.delegate import per_chat_id, create_open, pave_event_space
from telepot.loop import MessageLoop

import json
import time
import os
from argparse import ArgumentParser


class SmartIDReaderBot(telepot.helper.ChatHandler):
    def __init__(self, seed_tuple, smartid_engine, **kwargs):
        self.smartid_engine = smartid_engine

        super(SmartIDReaderBot, self).__init__(seed_tuple, **kwargs)

    def on_chat_message(self, msg):
        try:
            content_type, chat_type, chat_id = telepot.glance(msg)

            if content_type in ['document', 'photo']:
                content = msg[content_type] if content_type == 'document' else msg[content_type][-1]
                if 'file_id' in content:
                    # Creating downloads directory and downloading image file
                    downloads_dir = 'downloaded_images'
                    os.makedirs(downloads_dir, exist_ok=True)
                    temp_path = os.path.join(downloads_dir,
                                             'chat_%d_id_%d_temp.png' % (chat_id, msg['message_id']))
                    self.bot.download_file(content['file_id'], temp_path)

                    # Recognizing it and sending message with result
                    recognition_result_str = recognize_image_file(self.smartid_engine, temp_path)
                    self.send_message(recognition_result_str)
            else:
                self.send_message("Please send me a photo and I'll recognize it!")
        except Exception as e:
            self.send_message('Exception: %s' % e.message)

    def send_message(self, message):
        self.sender.sendMessage(message)
        print(message)


def recognize_image_file(smartid_engine, image_file_path):
    # Create session settings and enable document types
    session_settings = smartid_engine.CreateSessionSettings()
    session_settings.AddEnabledDocumentTypes('rus.passport.national')

    # Create recognition session
    session = smartid_engine.SpawnSession(session_settings)

    # Recognize image file
    result = session.ProcessImageFile(image_file_path)

    # Convert string fields from recognition results to dictionary
    recognized_fields = {}
    for field_name in result.GetStringFieldNames():
        field = result.GetStringField(field_name)
        recognized_fields[field_name] = field.GetValue().GetUtf8String()

    # Return JSON dictionary as string
    return json.dumps(recognized_fields, ensure_ascii=False, indent=2)


def main():
    parser = ArgumentParser()
    parser.add_argument('--token', type=str, required=True)
    parser.add_argument('--smartid-config', type=str, default='bundle_mock_smart_idreader.zip')
    args = parser.parse_args()

    # Creating recognition engine
    smartid_engine = se.RecognitionEngine(args.smartid_config)

    # Creating bot
    bot = telepot.DelegatorBot(args.token, [
        pave_event_space()(
            per_chat_id(), create_open,
            SmartIDReaderBot, smartid_engine, timeout=1000000
        )
    ])

    # Starting bot
    MessageLoop(bot).run_as_thread()
    print('Bot started, listening to messages...')

    while 1:
        time.sleep(10)


if __name__ == '__main__':
    main()
