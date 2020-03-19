# Copyright (c) 2012-2020, Smart Engines Ltd
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

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
import time
import os
import sys
from argparse import ArgumentParser

import pySmartIdEngine as se  # Smart IDReader by Smart Engines

class SmartIDReaderEngine():
    def __init__(self, config_path):
        self.smartid_engine = se.RecognitionEngine(config_path)
    
    def recognize_image_file(self, image_file_path):
        # Create session settings and enable document types
        session_settings = self.smartid_engine.CreateSessionSettings()
        session_settings.AddEnabledDocumentTypes('rus.passport.national')

        # Create recognition session
        session = self.smartid_engine.SpawnSession(session_settings)

        # Recognize image file
        result = session.ProcessImageFile(image_file_path)

        # Convert string fields from recognition results to dictionary
        recognized_fields = {}
        for field_name in result.GetStringFieldNames():
            field = result.GetStringField(field_name)
            recognized_fields[field_name] = field.GetValue().GetUtf8String()

        # Return JSON dictionary as string
        return json.dumps(recognized_fields, ensure_ascii=False, indent=2)

    def on_chat_photo(self, update, context):
        # Creating downloads directory and downloading photo
        temp_path = get_photo(update)

        # Recognizing it and sending message with result
        recognition_result_str = self.recognize_image_file(temp_path)
        update.message.reply_text(recognition_result_str)
        print(recognition_result_str)
        os.remove(temp_path)

    def on_chat_image(self, update, context):
        # Creating downloads directory and downloading image file
        temp_path = get_image(update)

        # Recognizing it and sending message with result
        recognition_result_str = self.recognize_image_file(temp_path)
        update.message.reply_text(recognition_result_str)
        print(recognition_result_str)
        os.remove(temp_path)

def get_photo(update):
    # Creating downloads directory and downloading image file
    downloads_dir = 'downloaded_images'
    os.makedirs(downloads_dir, exist_ok=True)
    temp_path = os.path.join(downloads_dir,
                                'file_%s_id_%d_temp.png' % (update.message.photo[-1].file_id, update.message.message_id))
    update.message.photo[-1].get_file().download(temp_path)
    return temp_path

def get_image(update):
    # Creating downloads directory and downloading image file
    downloads_dir = 'downloaded_images'
    os.makedirs(downloads_dir, exist_ok=True)
    temp_path = os.path.join(downloads_dir, update.message.document.file_name)
    update.message.document.get_file().download(custom_path = temp_path)
    return temp_path

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text("Please send me a photo and I'll recognize it!")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    parser = ArgumentParser()
    parser.add_argument('--token', type=str, )
    parser.add_argument('--smartid-config', type=str, default='bundle_mock_smart_idreader.zip')
    args = parser.parse_args()

    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary


    updater = Updater(args.token, use_context=True)

    # create an instance of SmartIdReader engine
    smartid_engine = SmartIDReaderEngine(args.smartid_config)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # on photo - recognize it with SmartIdReader
    dp.add_handler(MessageHandler(Filters.photo, smartid_engine.on_chat_photo))
    dp.add_handler(MessageHandler(Filters.document.image, smartid_engine.on_chat_image))
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
