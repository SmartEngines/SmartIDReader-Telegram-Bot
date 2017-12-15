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
 

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pySmartIdEngine')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pySmartIdEngine')
    _pySmartIdEngine = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pySmartIdEngine', [dirname(__file__)])
        except ImportError:
            import _pySmartIdEngine
            return _pySmartIdEngine
        try:
            _mod = imp.load_module('_pySmartIdEngine', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pySmartIdEngine = swig_import_helper()
    del swig_import_helper
else:
    import _pySmartIdEngine
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pySmartIdEngine.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _pySmartIdEngine.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _pySmartIdEngine.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _pySmartIdEngine.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _pySmartIdEngine.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _pySmartIdEngine.SwigPyIterator_equal(self, x)

    def copy(self):
        return _pySmartIdEngine.SwigPyIterator_copy(self)

    def next(self):
        return _pySmartIdEngine.SwigPyIterator_next(self)

    def __next__(self):
        return _pySmartIdEngine.SwigPyIterator___next__(self)

    def previous(self):
        return _pySmartIdEngine.SwigPyIterator_previous(self)

    def advance(self, n):
        return _pySmartIdEngine.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _pySmartIdEngine.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _pySmartIdEngine.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _pySmartIdEngine.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _pySmartIdEngine.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _pySmartIdEngine.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _pySmartIdEngine.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _pySmartIdEngine.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class Rectangle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Rectangle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Rectangle, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pySmartIdEngine.new_Rectangle(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["x"] = _pySmartIdEngine.Rectangle_x_set
    __swig_getmethods__["x"] = _pySmartIdEngine.Rectangle_x_get
    if _newclass:
        x = _swig_property(_pySmartIdEngine.Rectangle_x_get, _pySmartIdEngine.Rectangle_x_set)
    __swig_setmethods__["y"] = _pySmartIdEngine.Rectangle_y_set
    __swig_getmethods__["y"] = _pySmartIdEngine.Rectangle_y_get
    if _newclass:
        y = _swig_property(_pySmartIdEngine.Rectangle_y_get, _pySmartIdEngine.Rectangle_y_set)
    __swig_setmethods__["width"] = _pySmartIdEngine.Rectangle_width_set
    __swig_getmethods__["width"] = _pySmartIdEngine.Rectangle_width_get
    if _newclass:
        width = _swig_property(_pySmartIdEngine.Rectangle_width_get, _pySmartIdEngine.Rectangle_width_set)
    __swig_setmethods__["height"] = _pySmartIdEngine.Rectangle_height_set
    __swig_getmethods__["height"] = _pySmartIdEngine.Rectangle_height_get
    if _newclass:
        height = _swig_property(_pySmartIdEngine.Rectangle_height_get, _pySmartIdEngine.Rectangle_height_set)
    __swig_destroy__ = _pySmartIdEngine.delete_Rectangle
    __del__ = lambda self: None
Rectangle_swigregister = _pySmartIdEngine.Rectangle_swigregister
Rectangle_swigregister(Rectangle)

class Point(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Point, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Point, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pySmartIdEngine.new_Point(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["x"] = _pySmartIdEngine.Point_x_set
    __swig_getmethods__["x"] = _pySmartIdEngine.Point_x_get
    if _newclass:
        x = _swig_property(_pySmartIdEngine.Point_x_get, _pySmartIdEngine.Point_x_set)
    __swig_setmethods__["y"] = _pySmartIdEngine.Point_y_set
    __swig_getmethods__["y"] = _pySmartIdEngine.Point_y_get
    if _newclass:
        y = _swig_property(_pySmartIdEngine.Point_y_get, _pySmartIdEngine.Point_y_set)
    __swig_destroy__ = _pySmartIdEngine.delete_Point
    __del__ = lambda self: None
Point_swigregister = _pySmartIdEngine.Point_swigregister
Point_swigregister(Point)

class Quadrangle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Quadrangle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Quadrangle, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pySmartIdEngine.new_Quadrangle(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def GetPoint(self, index):
        return _pySmartIdEngine.Quadrangle_GetPoint(self, index)

    def SetPoint(self, index, value):
        return _pySmartIdEngine.Quadrangle_SetPoint(self, index, value)
    __swig_destroy__ = _pySmartIdEngine.delete_Quadrangle
    __del__ = lambda self: None
Quadrangle_swigregister = _pySmartIdEngine.Quadrangle_swigregister
Quadrangle_swigregister(Quadrangle)

class Image(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Image, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Image, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pySmartIdEngine.new_Image(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pySmartIdEngine.delete_Image
    __del__ = lambda self: None

    def Save(self, image_filename):
        return _pySmartIdEngine.Image_Save(self, image_filename)

    def GetRequiredBufferLength(self):
        return _pySmartIdEngine.Image_GetRequiredBufferLength(self)

    def CopyToBuffer(self, out_buffer, buffer_length):
        return _pySmartIdEngine.Image_CopyToBuffer(self, out_buffer, buffer_length)

    def GetRequiredBase64BufferLength(self):
        return _pySmartIdEngine.Image_GetRequiredBase64BufferLength(self)

    def CopyBase64ToBuffer(self, out_buffer, buffer_length):
        return _pySmartIdEngine.Image_CopyBase64ToBuffer(self, out_buffer, buffer_length)

    def Clear(self):
        return _pySmartIdEngine.Image_Clear(self)

    def GetWidth(self):
        return _pySmartIdEngine.Image_GetWidth(self)

    def GetHeight(self):
        return _pySmartIdEngine.Image_GetHeight(self)

    def GetChannels(self):
        return _pySmartIdEngine.Image_GetChannels(self)

    def IsMemoryOwner(self):
        return _pySmartIdEngine.Image_IsMemoryOwner(self)

    def ForceMemoryOwner(self):
        return _pySmartIdEngine.Image_ForceMemoryOwner(self)

    def Resize(self, new_width, new_height):
        return _pySmartIdEngine.Image_Resize(self, new_width, new_height)
    __swig_setmethods__["width"] = _pySmartIdEngine.Image_width_set
    __swig_getmethods__["width"] = _pySmartIdEngine.Image_width_get
    if _newclass:
        width = _swig_property(_pySmartIdEngine.Image_width_get, _pySmartIdEngine.Image_width_set)
    __swig_setmethods__["height"] = _pySmartIdEngine.Image_height_set
    __swig_getmethods__["height"] = _pySmartIdEngine.Image_height_get
    if _newclass:
        height = _swig_property(_pySmartIdEngine.Image_height_get, _pySmartIdEngine.Image_height_set)
    __swig_setmethods__["stride"] = _pySmartIdEngine.Image_stride_set
    __swig_getmethods__["stride"] = _pySmartIdEngine.Image_stride_get
    if _newclass:
        stride = _swig_property(_pySmartIdEngine.Image_stride_get, _pySmartIdEngine.Image_stride_set)
    __swig_setmethods__["channels"] = _pySmartIdEngine.Image_channels_set
    __swig_getmethods__["channels"] = _pySmartIdEngine.Image_channels_get
    if _newclass:
        channels = _swig_property(_pySmartIdEngine.Image_channels_get, _pySmartIdEngine.Image_channels_set)
Image_swigregister = _pySmartIdEngine.Image_swigregister
Image_swigregister(Image)

Landscape = _pySmartIdEngine.Landscape
Portrait = _pySmartIdEngine.Portrait
InvertedLandscape = _pySmartIdEngine.InvertedLandscape
InvertedPortrait = _pySmartIdEngine.InvertedPortrait
class OcrCharVariant(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OcrCharVariant, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OcrCharVariant, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _pySmartIdEngine.delete_OcrCharVariant
    __del__ = lambda self: None

    def __init__(self, *args):
        this = _pySmartIdEngine.new_OcrCharVariant(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def GetUtf16Character(self):
        return _pySmartIdEngine.OcrCharVariant_GetUtf16Character(self)

    def GetUtf8Character(self):
        return _pySmartIdEngine.OcrCharVariant_GetUtf8Character(self)

    def GetConfidence(self):
        return _pySmartIdEngine.OcrCharVariant_GetConfidence(self)
OcrCharVariant_swigregister = _pySmartIdEngine.OcrCharVariant_swigregister
OcrCharVariant_swigregister(OcrCharVariant)

class OcrChar(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OcrChar, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OcrChar, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pySmartIdEngine.new_OcrChar(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pySmartIdEngine.delete_OcrChar
    __del__ = lambda self: None

    def GetOcrCharVariants(self):
        return _pySmartIdEngine.OcrChar_GetOcrCharVariants(self)

    def IsHighlighted(self):
        return _pySmartIdEngine.OcrChar_IsHighlighted(self)

    def IsCorrected(self):
        return _pySmartIdEngine.OcrChar_IsCorrected(self)

    def GetUtf16Character(self):
        return _pySmartIdEngine.OcrChar_GetUtf16Character(self)

    def GetUtf8Character(self):
        return _pySmartIdEngine.OcrChar_GetUtf8Character(self)
OcrChar_swigregister = _pySmartIdEngine.OcrChar_swigregister
OcrChar_swigregister(OcrChar)

class OcrString(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OcrString, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OcrString, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pySmartIdEngine.new_OcrString(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pySmartIdEngine.delete_OcrString
    __del__ = lambda self: None

    def GetOcrChars(self):
        return _pySmartIdEngine.OcrString_GetOcrChars(self)

    def GetUtf8String(self):
        return _pySmartIdEngine.OcrString_GetUtf8String(self)

    def GetUtf16String(self):
        return _pySmartIdEngine.OcrString_GetUtf16String(self)
OcrString_swigregister = _pySmartIdEngine.OcrString_swigregister
OcrString_swigregister(OcrString)

class StringField(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringField, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringField, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pySmartIdEngine.new_StringField(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def GetName(self):
        return _pySmartIdEngine.StringField_GetName(self)

    def GetValue(self):
        return _pySmartIdEngine.StringField_GetValue(self)

    def GetUtf8Value(self):
        return _pySmartIdEngine.StringField_GetUtf8Value(self)

    def GetRawValue(self):
        return _pySmartIdEngine.StringField_GetRawValue(self)

    def GetUtf8RawValue(self):
        return _pySmartIdEngine.StringField_GetUtf8RawValue(self)

    def IsAccepted(self):
        return _pySmartIdEngine.StringField_IsAccepted(self)

    def GetConfidence(self):
        return _pySmartIdEngine.StringField_GetConfidence(self)
    __swig_destroy__ = _pySmartIdEngine.delete_StringField
    __del__ = lambda self: None
StringField_swigregister = _pySmartIdEngine.StringField_swigregister
StringField_swigregister(StringField)

class ImageField(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ImageField, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ImageField, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pySmartIdEngine.new_ImageField(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pySmartIdEngine.delete_ImageField
    __del__ = lambda self: None

    def GetName(self):
        return _pySmartIdEngine.ImageField_GetName(self)

    def GetValue(self):
        return _pySmartIdEngine.ImageField_GetValue(self)

    def IsAccepted(self):
        return _pySmartIdEngine.ImageField_IsAccepted(self)

    def GetConfidence(self):
        return _pySmartIdEngine.ImageField_GetConfidence(self)
ImageField_swigregister = _pySmartIdEngine.ImageField_swigregister
ImageField_swigregister(ImageField)

class MatchResult(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MatchResult, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MatchResult, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pySmartIdEngine.new_MatchResult(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def GetTemplateType(self):
        return _pySmartIdEngine.MatchResult_GetTemplateType(self)

    def GetQuadrangle(self):
        return _pySmartIdEngine.MatchResult_GetQuadrangle(self)

    def GetStandardWidth(self):
        return _pySmartIdEngine.MatchResult_GetStandardWidth(self)

    def GetStandardHeight(self):
        return _pySmartIdEngine.MatchResult_GetStandardHeight(self)

    def GetAccepted(self):
        return _pySmartIdEngine.MatchResult_GetAccepted(self)
    __swig_setmethods__["templateType"] = _pySmartIdEngine.MatchResult_templateType_set
    __swig_getmethods__["templateType"] = _pySmartIdEngine.MatchResult_templateType_get
    if _newclass:
        templateType = _swig_property(_pySmartIdEngine.MatchResult_templateType_get, _pySmartIdEngine.MatchResult_templateType_set)
    __swig_setmethods__["quadrangle"] = _pySmartIdEngine.MatchResult_quadrangle_set
    __swig_getmethods__["quadrangle"] = _pySmartIdEngine.MatchResult_quadrangle_get
    if _newclass:
        quadrangle = _swig_property(_pySmartIdEngine.MatchResult_quadrangle_get, _pySmartIdEngine.MatchResult_quadrangle_set)
    __swig_setmethods__["standardWidth"] = _pySmartIdEngine.MatchResult_standardWidth_set
    __swig_getmethods__["standardWidth"] = _pySmartIdEngine.MatchResult_standardWidth_get
    if _newclass:
        standardWidth = _swig_property(_pySmartIdEngine.MatchResult_standardWidth_get, _pySmartIdEngine.MatchResult_standardWidth_set)
    __swig_setmethods__["standardHeight"] = _pySmartIdEngine.MatchResult_standardHeight_set
    __swig_getmethods__["standardHeight"] = _pySmartIdEngine.MatchResult_standardHeight_get
    if _newclass:
        standardHeight = _swig_property(_pySmartIdEngine.MatchResult_standardHeight_get, _pySmartIdEngine.MatchResult_standardHeight_set)
    __swig_setmethods__["accepted"] = _pySmartIdEngine.MatchResult_accepted_set
    __swig_getmethods__["accepted"] = _pySmartIdEngine.MatchResult_accepted_get
    if _newclass:
        accepted = _swig_property(_pySmartIdEngine.MatchResult_accepted_get, _pySmartIdEngine.MatchResult_accepted_set)
    __swig_destroy__ = _pySmartIdEngine.delete_MatchResult
    __del__ = lambda self: None
MatchResult_swigregister = _pySmartIdEngine.MatchResult_swigregister
MatchResult_swigregister(MatchResult)

class SegmentationResult(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SegmentationResult, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SegmentationResult, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pySmartIdEngine.new_SegmentationResult(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def GetZoneNames(self):
        return _pySmartIdEngine.SegmentationResult_GetZoneNames(self)

    def HasZoneQuadrangle(self, zone_name):
        return _pySmartIdEngine.SegmentationResult_HasZoneQuadrangle(self, zone_name)

    def GetZoneQuadrangle(self, zone_name):
        return _pySmartIdEngine.SegmentationResult_GetZoneQuadrangle(self, zone_name)

    def GetZoneQuadrangles(self):
        return _pySmartIdEngine.SegmentationResult_GetZoneQuadrangles(self)

    def GetZoneFieldName(self, zone_name):
        return _pySmartIdEngine.SegmentationResult_GetZoneFieldName(self, zone_name)

    def GetAccepted(self):
        return _pySmartIdEngine.SegmentationResult_GetAccepted(self)
    __swig_destroy__ = _pySmartIdEngine.delete_SegmentationResult
    __del__ = lambda self: None
SegmentationResult_swigregister = _pySmartIdEngine.SegmentationResult_swigregister
SegmentationResult_swigregister(SegmentationResult)

class RecognitionResult(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RecognitionResult, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RecognitionResult, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pySmartIdEngine.new_RecognitionResult(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pySmartIdEngine.delete_RecognitionResult
    __del__ = lambda self: None

    def GetStringFieldNames(self):
        return _pySmartIdEngine.RecognitionResult_GetStringFieldNames(self)

    def HasStringField(self, name):
        return _pySmartIdEngine.RecognitionResult_HasStringField(self, name)

    def GetStringField(self, name):
        return _pySmartIdEngine.RecognitionResult_GetStringField(self, name)

    def GetStringFields(self, *args):
        return _pySmartIdEngine.RecognitionResult_GetStringFields(self, *args)

    def SetStringFields(self, string_fields):
        return _pySmartIdEngine.RecognitionResult_SetStringFields(self, string_fields)

    def GetImageFieldNames(self):
        return _pySmartIdEngine.RecognitionResult_GetImageFieldNames(self)

    def HasImageField(self, name):
        return _pySmartIdEngine.RecognitionResult_HasImageField(self, name)

    def GetImageField(self, name):
        return _pySmartIdEngine.RecognitionResult_GetImageField(self, name)

    def GetImageFields(self, *args):
        return _pySmartIdEngine.RecognitionResult_GetImageFields(self, *args)

    def SetImageFields(self, image_fields):
        return _pySmartIdEngine.RecognitionResult_SetImageFields(self, image_fields)

    def GetDocumentType(self):
        return _pySmartIdEngine.RecognitionResult_GetDocumentType(self)

    def SetDocumentType(self, doctype):
        return _pySmartIdEngine.RecognitionResult_SetDocumentType(self, doctype)

    def GetMatchResults(self):
        return _pySmartIdEngine.RecognitionResult_GetMatchResults(self)

    def SetMatchResults(self, match_results):
        return _pySmartIdEngine.RecognitionResult_SetMatchResults(self, match_results)

    def GetSegmentationResults(self):
        return _pySmartIdEngine.RecognitionResult_GetSegmentationResults(self)

    def SetSegmentationResults(self, segmentation_results):
        return _pySmartIdEngine.RecognitionResult_SetSegmentationResults(self, segmentation_results)

    def IsTerminal(self):
        return _pySmartIdEngine.RecognitionResult_IsTerminal(self)

    def SetIsTerminal(self, is_terminal):
        return _pySmartIdEngine.RecognitionResult_SetIsTerminal(self, is_terminal)
RecognitionResult_swigregister = _pySmartIdEngine.RecognitionResult_swigregister
RecognitionResult_swigregister(RecognitionResult)

class ResultReporterInterface(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ResultReporterInterface, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ResultReporterInterface, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SnapshotRejected(self):
        return _pySmartIdEngine.ResultReporterInterface_SnapshotRejected(self)

    def DocumentMatched(self, match_results):
        return _pySmartIdEngine.ResultReporterInterface_DocumentMatched(self, match_results)

    def DocumentSegmented(self, segmentation_results):
        return _pySmartIdEngine.ResultReporterInterface_DocumentSegmented(self, segmentation_results)

    def SnapshotProcessed(self, recog_result):
        return _pySmartIdEngine.ResultReporterInterface_SnapshotProcessed(self, recog_result)

    def SessionEnded(self):
        return _pySmartIdEngine.ResultReporterInterface_SessionEnded(self)
    __swig_destroy__ = _pySmartIdEngine.delete_ResultReporterInterface
    __del__ = lambda self: None
ResultReporterInterface_swigregister = _pySmartIdEngine.ResultReporterInterface_swigregister
ResultReporterInterface_swigregister(ResultReporterInterface)

class SessionSettings(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SessionSettings, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SessionSettings, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pySmartIdEngine.delete_SessionSettings
    __del__ = lambda self: None

    def Clone(self):
        return _pySmartIdEngine.SessionSettings_Clone(self)

    def GetEnabledDocumentTypes(self):
        return _pySmartIdEngine.SessionSettings_GetEnabledDocumentTypes(self)

    def AddEnabledDocumentTypes(self, doctype_mask):
        return _pySmartIdEngine.SessionSettings_AddEnabledDocumentTypes(self, doctype_mask)

    def RemoveEnabledDocumentTypes(self, doctype_mask):
        return _pySmartIdEngine.SessionSettings_RemoveEnabledDocumentTypes(self, doctype_mask)

    def SetEnabledDocumentTypes(self, document_types):
        return _pySmartIdEngine.SessionSettings_SetEnabledDocumentTypes(self, document_types)

    def GetSupportedDocumentTypes(self):
        return _pySmartIdEngine.SessionSettings_GetSupportedDocumentTypes(self)

    def GetOptionNames(self):
        return _pySmartIdEngine.SessionSettings_GetOptionNames(self)

    def HasOption(self, name):
        return _pySmartIdEngine.SessionSettings_HasOption(self, name)

    def GetOption(self, name):
        return _pySmartIdEngine.SessionSettings_GetOption(self, name)

    def SetOption(self, name, value):
        return _pySmartIdEngine.SessionSettings_SetOption(self, name, value)

    def RemoveOption(self, name):
        return _pySmartIdEngine.SessionSettings_RemoveOption(self, name)

    def GetEnabledStringFieldNames(self):
        return _pySmartIdEngine.SessionSettings_GetEnabledStringFieldNames(self)

    def EnableStringField(self, doctype, string_field_name):
        return _pySmartIdEngine.SessionSettings_EnableStringField(self, doctype, string_field_name)

    def DisableStringField(self, doctype, string_field_name):
        return _pySmartIdEngine.SessionSettings_DisableStringField(self, doctype, string_field_name)

    def SetEnabledStringFields(self, doctype, string_field_names):
        return _pySmartIdEngine.SessionSettings_SetEnabledStringFields(self, doctype, string_field_names)

    def GetSupportedFieldNames(self, doctype):
        return _pySmartIdEngine.SessionSettings_GetSupportedFieldNames(self, doctype)
SessionSettings_swigregister = _pySmartIdEngine.SessionSettings_swigregister
SessionSettings_swigregister(SessionSettings)

class RecognitionSession(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RecognitionSession, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RecognitionSession, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pySmartIdEngine.delete_RecognitionSession
    __del__ = lambda self: None

    def ProcessSnapshot(self, *args):
        return _pySmartIdEngine.RecognitionSession_ProcessSnapshot(self, *args)

    def ProcessYUVSnapshot(self, *args):
        return _pySmartIdEngine.RecognitionSession_ProcessYUVSnapshot(self, *args)

    def ProcessImage(self, *args):
        return _pySmartIdEngine.RecognitionSession_ProcessImage(self, *args)

    def ProcessImageFile(self, *args):
        return _pySmartIdEngine.RecognitionSession_ProcessImageFile(self, *args)

    def Reset(self):
        return _pySmartIdEngine.RecognitionSession_Reset(self)
RecognitionSession_swigregister = _pySmartIdEngine.RecognitionSession_swigregister
RecognitionSession_swigregister(RecognitionSession)

class RecognitionEngine(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RecognitionEngine, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RecognitionEngine, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pySmartIdEngine.new_RecognitionEngine(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pySmartIdEngine.delete_RecognitionEngine
    __del__ = lambda self: None

    def CreateSessionSettings(self):
        return _pySmartIdEngine.RecognitionEngine_CreateSessionSettings(self)

    def SpawnSession(self, session_settings, result_reporter=None):
        return _pySmartIdEngine.RecognitionEngine_SpawnSession(self, session_settings, result_reporter)
    if _newclass:
        GetVersion = staticmethod(_pySmartIdEngine.RecognitionEngine_GetVersion)
    else:
        GetVersion = _pySmartIdEngine.RecognitionEngine_GetVersion
RecognitionEngine_swigregister = _pySmartIdEngine.RecognitionEngine_swigregister
RecognitionEngine_swigregister(RecognitionEngine)

def RecognitionEngine_GetVersion():
    return _pySmartIdEngine.RecognitionEngine_GetVersion()
RecognitionEngine_GetVersion = _pySmartIdEngine.RecognitionEngine_GetVersion

class Utf16CharVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Utf16CharVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Utf16CharVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pySmartIdEngine.Utf16CharVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pySmartIdEngine.Utf16CharVector___nonzero__(self)

    def __bool__(self):
        return _pySmartIdEngine.Utf16CharVector___bool__(self)

    def __len__(self):
        return _pySmartIdEngine.Utf16CharVector___len__(self)

    def __getslice__(self, i, j):
        return _pySmartIdEngine.Utf16CharVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pySmartIdEngine.Utf16CharVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pySmartIdEngine.Utf16CharVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pySmartIdEngine.Utf16CharVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pySmartIdEngine.Utf16CharVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pySmartIdEngine.Utf16CharVector___setitem__(self, *args)

    def pop(self):
        return _pySmartIdEngine.Utf16CharVector_pop(self)

    def append(self, x):
        return _pySmartIdEngine.Utf16CharVector_append(self, x)

    def empty(self):
        return _pySmartIdEngine.Utf16CharVector_empty(self)

    def size(self):
        return _pySmartIdEngine.Utf16CharVector_size(self)

    def swap(self, v):
        return _pySmartIdEngine.Utf16CharVector_swap(self, v)

    def begin(self):
        return _pySmartIdEngine.Utf16CharVector_begin(self)

    def end(self):
        return _pySmartIdEngine.Utf16CharVector_end(self)

    def rbegin(self):
        return _pySmartIdEngine.Utf16CharVector_rbegin(self)

    def rend(self):
        return _pySmartIdEngine.Utf16CharVector_rend(self)

    def clear(self):
        return _pySmartIdEngine.Utf16CharVector_clear(self)

    def get_allocator(self):
        return _pySmartIdEngine.Utf16CharVector_get_allocator(self)

    def pop_back(self):
        return _pySmartIdEngine.Utf16CharVector_pop_back(self)

    def erase(self, *args):
        return _pySmartIdEngine.Utf16CharVector_erase(self, *args)

    def __init__(self, *args):
        this = _pySmartIdEngine.new_Utf16CharVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _pySmartIdEngine.Utf16CharVector_push_back(self, x)

    def front(self):
        return _pySmartIdEngine.Utf16CharVector_front(self)

    def back(self):
        return _pySmartIdEngine.Utf16CharVector_back(self)

    def assign(self, n, x):
        return _pySmartIdEngine.Utf16CharVector_assign(self, n, x)

    def resize(self, *args):
        return _pySmartIdEngine.Utf16CharVector_resize(self, *args)

    def insert(self, *args):
        return _pySmartIdEngine.Utf16CharVector_insert(self, *args)

    def reserve(self, n):
        return _pySmartIdEngine.Utf16CharVector_reserve(self, n)

    def capacity(self):
        return _pySmartIdEngine.Utf16CharVector_capacity(self)
    __swig_destroy__ = _pySmartIdEngine.delete_Utf16CharVector
    __del__ = lambda self: None
Utf16CharVector_swigregister = _pySmartIdEngine.Utf16CharVector_swigregister
Utf16CharVector_swigregister(Utf16CharVector)

class StringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pySmartIdEngine.StringVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pySmartIdEngine.StringVector___nonzero__(self)

    def __bool__(self):
        return _pySmartIdEngine.StringVector___bool__(self)

    def __len__(self):
        return _pySmartIdEngine.StringVector___len__(self)

    def __getslice__(self, i, j):
        return _pySmartIdEngine.StringVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pySmartIdEngine.StringVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pySmartIdEngine.StringVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pySmartIdEngine.StringVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pySmartIdEngine.StringVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pySmartIdEngine.StringVector___setitem__(self, *args)

    def pop(self):
        return _pySmartIdEngine.StringVector_pop(self)

    def append(self, x):
        return _pySmartIdEngine.StringVector_append(self, x)

    def empty(self):
        return _pySmartIdEngine.StringVector_empty(self)

    def size(self):
        return _pySmartIdEngine.StringVector_size(self)

    def swap(self, v):
        return _pySmartIdEngine.StringVector_swap(self, v)

    def begin(self):
        return _pySmartIdEngine.StringVector_begin(self)

    def end(self):
        return _pySmartIdEngine.StringVector_end(self)

    def rbegin(self):
        return _pySmartIdEngine.StringVector_rbegin(self)

    def rend(self):
        return _pySmartIdEngine.StringVector_rend(self)

    def clear(self):
        return _pySmartIdEngine.StringVector_clear(self)

    def get_allocator(self):
        return _pySmartIdEngine.StringVector_get_allocator(self)

    def pop_back(self):
        return _pySmartIdEngine.StringVector_pop_back(self)

    def erase(self, *args):
        return _pySmartIdEngine.StringVector_erase(self, *args)

    def __init__(self, *args):
        this = _pySmartIdEngine.new_StringVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _pySmartIdEngine.StringVector_push_back(self, x)

    def front(self):
        return _pySmartIdEngine.StringVector_front(self)

    def back(self):
        return _pySmartIdEngine.StringVector_back(self)

    def assign(self, n, x):
        return _pySmartIdEngine.StringVector_assign(self, n, x)

    def resize(self, *args):
        return _pySmartIdEngine.StringVector_resize(self, *args)

    def insert(self, *args):
        return _pySmartIdEngine.StringVector_insert(self, *args)

    def reserve(self, n):
        return _pySmartIdEngine.StringVector_reserve(self, n)

    def capacity(self):
        return _pySmartIdEngine.StringVector_capacity(self)
    __swig_destroy__ = _pySmartIdEngine.delete_StringVector
    __del__ = lambda self: None
StringVector_swigregister = _pySmartIdEngine.StringVector_swigregister
StringVector_swigregister(StringVector)

class StringVector2d(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVector2d, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVector2d, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pySmartIdEngine.StringVector2d_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pySmartIdEngine.StringVector2d___nonzero__(self)

    def __bool__(self):
        return _pySmartIdEngine.StringVector2d___bool__(self)

    def __len__(self):
        return _pySmartIdEngine.StringVector2d___len__(self)

    def __getslice__(self, i, j):
        return _pySmartIdEngine.StringVector2d___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pySmartIdEngine.StringVector2d___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pySmartIdEngine.StringVector2d___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pySmartIdEngine.StringVector2d___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pySmartIdEngine.StringVector2d___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pySmartIdEngine.StringVector2d___setitem__(self, *args)

    def pop(self):
        return _pySmartIdEngine.StringVector2d_pop(self)

    def append(self, x):
        return _pySmartIdEngine.StringVector2d_append(self, x)

    def empty(self):
        return _pySmartIdEngine.StringVector2d_empty(self)

    def size(self):
        return _pySmartIdEngine.StringVector2d_size(self)

    def swap(self, v):
        return _pySmartIdEngine.StringVector2d_swap(self, v)

    def begin(self):
        return _pySmartIdEngine.StringVector2d_begin(self)

    def end(self):
        return _pySmartIdEngine.StringVector2d_end(self)

    def rbegin(self):
        return _pySmartIdEngine.StringVector2d_rbegin(self)

    def rend(self):
        return _pySmartIdEngine.StringVector2d_rend(self)

    def clear(self):
        return _pySmartIdEngine.StringVector2d_clear(self)

    def get_allocator(self):
        return _pySmartIdEngine.StringVector2d_get_allocator(self)

    def pop_back(self):
        return _pySmartIdEngine.StringVector2d_pop_back(self)

    def erase(self, *args):
        return _pySmartIdEngine.StringVector2d_erase(self, *args)

    def __init__(self, *args):
        this = _pySmartIdEngine.new_StringVector2d(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _pySmartIdEngine.StringVector2d_push_back(self, x)

    def front(self):
        return _pySmartIdEngine.StringVector2d_front(self)

    def back(self):
        return _pySmartIdEngine.StringVector2d_back(self)

    def assign(self, n, x):
        return _pySmartIdEngine.StringVector2d_assign(self, n, x)

    def resize(self, *args):
        return _pySmartIdEngine.StringVector2d_resize(self, *args)

    def insert(self, *args):
        return _pySmartIdEngine.StringVector2d_insert(self, *args)

    def reserve(self, n):
        return _pySmartIdEngine.StringVector2d_reserve(self, n)

    def capacity(self):
        return _pySmartIdEngine.StringVector2d_capacity(self)
    __swig_destroy__ = _pySmartIdEngine.delete_StringVector2d
    __del__ = lambda self: None
StringVector2d_swigregister = _pySmartIdEngine.StringVector2d_swigregister
StringVector2d_swigregister(StringVector2d)

class OcrCharVariantVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OcrCharVariantVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OcrCharVariantVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pySmartIdEngine.OcrCharVariantVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pySmartIdEngine.OcrCharVariantVector___nonzero__(self)

    def __bool__(self):
        return _pySmartIdEngine.OcrCharVariantVector___bool__(self)

    def __len__(self):
        return _pySmartIdEngine.OcrCharVariantVector___len__(self)

    def __getslice__(self, i, j):
        return _pySmartIdEngine.OcrCharVariantVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pySmartIdEngine.OcrCharVariantVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pySmartIdEngine.OcrCharVariantVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pySmartIdEngine.OcrCharVariantVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pySmartIdEngine.OcrCharVariantVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pySmartIdEngine.OcrCharVariantVector___setitem__(self, *args)

    def pop(self):
        return _pySmartIdEngine.OcrCharVariantVector_pop(self)

    def append(self, x):
        return _pySmartIdEngine.OcrCharVariantVector_append(self, x)

    def empty(self):
        return _pySmartIdEngine.OcrCharVariantVector_empty(self)

    def size(self):
        return _pySmartIdEngine.OcrCharVariantVector_size(self)

    def swap(self, v):
        return _pySmartIdEngine.OcrCharVariantVector_swap(self, v)

    def begin(self):
        return _pySmartIdEngine.OcrCharVariantVector_begin(self)

    def end(self):
        return _pySmartIdEngine.OcrCharVariantVector_end(self)

    def rbegin(self):
        return _pySmartIdEngine.OcrCharVariantVector_rbegin(self)

    def rend(self):
        return _pySmartIdEngine.OcrCharVariantVector_rend(self)

    def clear(self):
        return _pySmartIdEngine.OcrCharVariantVector_clear(self)

    def get_allocator(self):
        return _pySmartIdEngine.OcrCharVariantVector_get_allocator(self)

    def pop_back(self):
        return _pySmartIdEngine.OcrCharVariantVector_pop_back(self)

    def erase(self, *args):
        return _pySmartIdEngine.OcrCharVariantVector_erase(self, *args)

    def __init__(self, *args):
        this = _pySmartIdEngine.new_OcrCharVariantVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _pySmartIdEngine.OcrCharVariantVector_push_back(self, x)

    def front(self):
        return _pySmartIdEngine.OcrCharVariantVector_front(self)

    def back(self):
        return _pySmartIdEngine.OcrCharVariantVector_back(self)

    def assign(self, n, x):
        return _pySmartIdEngine.OcrCharVariantVector_assign(self, n, x)

    def resize(self, *args):
        return _pySmartIdEngine.OcrCharVariantVector_resize(self, *args)

    def insert(self, *args):
        return _pySmartIdEngine.OcrCharVariantVector_insert(self, *args)

    def reserve(self, n):
        return _pySmartIdEngine.OcrCharVariantVector_reserve(self, n)

    def capacity(self):
        return _pySmartIdEngine.OcrCharVariantVector_capacity(self)
    __swig_destroy__ = _pySmartIdEngine.delete_OcrCharVariantVector
    __del__ = lambda self: None
OcrCharVariantVector_swigregister = _pySmartIdEngine.OcrCharVariantVector_swigregister
OcrCharVariantVector_swigregister(OcrCharVariantVector)

class OcrCharVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OcrCharVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OcrCharVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pySmartIdEngine.OcrCharVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pySmartIdEngine.OcrCharVector___nonzero__(self)

    def __bool__(self):
        return _pySmartIdEngine.OcrCharVector___bool__(self)

    def __len__(self):
        return _pySmartIdEngine.OcrCharVector___len__(self)

    def __getslice__(self, i, j):
        return _pySmartIdEngine.OcrCharVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pySmartIdEngine.OcrCharVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pySmartIdEngine.OcrCharVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pySmartIdEngine.OcrCharVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pySmartIdEngine.OcrCharVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pySmartIdEngine.OcrCharVector___setitem__(self, *args)

    def pop(self):
        return _pySmartIdEngine.OcrCharVector_pop(self)

    def append(self, x):
        return _pySmartIdEngine.OcrCharVector_append(self, x)

    def empty(self):
        return _pySmartIdEngine.OcrCharVector_empty(self)

    def size(self):
        return _pySmartIdEngine.OcrCharVector_size(self)

    def swap(self, v):
        return _pySmartIdEngine.OcrCharVector_swap(self, v)

    def begin(self):
        return _pySmartIdEngine.OcrCharVector_begin(self)

    def end(self):
        return _pySmartIdEngine.OcrCharVector_end(self)

    def rbegin(self):
        return _pySmartIdEngine.OcrCharVector_rbegin(self)

    def rend(self):
        return _pySmartIdEngine.OcrCharVector_rend(self)

    def clear(self):
        return _pySmartIdEngine.OcrCharVector_clear(self)

    def get_allocator(self):
        return _pySmartIdEngine.OcrCharVector_get_allocator(self)

    def pop_back(self):
        return _pySmartIdEngine.OcrCharVector_pop_back(self)

    def erase(self, *args):
        return _pySmartIdEngine.OcrCharVector_erase(self, *args)

    def __init__(self, *args):
        this = _pySmartIdEngine.new_OcrCharVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _pySmartIdEngine.OcrCharVector_push_back(self, x)

    def front(self):
        return _pySmartIdEngine.OcrCharVector_front(self)

    def back(self):
        return _pySmartIdEngine.OcrCharVector_back(self)

    def assign(self, n, x):
        return _pySmartIdEngine.OcrCharVector_assign(self, n, x)

    def resize(self, *args):
        return _pySmartIdEngine.OcrCharVector_resize(self, *args)

    def insert(self, *args):
        return _pySmartIdEngine.OcrCharVector_insert(self, *args)

    def reserve(self, n):
        return _pySmartIdEngine.OcrCharVector_reserve(self, n)

    def capacity(self):
        return _pySmartIdEngine.OcrCharVector_capacity(self)
    __swig_destroy__ = _pySmartIdEngine.delete_OcrCharVector
    __del__ = lambda self: None
OcrCharVector_swigregister = _pySmartIdEngine.OcrCharVector_swigregister
OcrCharVector_swigregister(OcrCharVector)

class MatchResultVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MatchResultVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MatchResultVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pySmartIdEngine.MatchResultVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pySmartIdEngine.MatchResultVector___nonzero__(self)

    def __bool__(self):
        return _pySmartIdEngine.MatchResultVector___bool__(self)

    def __len__(self):
        return _pySmartIdEngine.MatchResultVector___len__(self)

    def __getslice__(self, i, j):
        return _pySmartIdEngine.MatchResultVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pySmartIdEngine.MatchResultVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pySmartIdEngine.MatchResultVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pySmartIdEngine.MatchResultVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pySmartIdEngine.MatchResultVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pySmartIdEngine.MatchResultVector___setitem__(self, *args)

    def pop(self):
        return _pySmartIdEngine.MatchResultVector_pop(self)

    def append(self, x):
        return _pySmartIdEngine.MatchResultVector_append(self, x)

    def empty(self):
        return _pySmartIdEngine.MatchResultVector_empty(self)

    def size(self):
        return _pySmartIdEngine.MatchResultVector_size(self)

    def swap(self, v):
        return _pySmartIdEngine.MatchResultVector_swap(self, v)

    def begin(self):
        return _pySmartIdEngine.MatchResultVector_begin(self)

    def end(self):
        return _pySmartIdEngine.MatchResultVector_end(self)

    def rbegin(self):
        return _pySmartIdEngine.MatchResultVector_rbegin(self)

    def rend(self):
        return _pySmartIdEngine.MatchResultVector_rend(self)

    def clear(self):
        return _pySmartIdEngine.MatchResultVector_clear(self)

    def get_allocator(self):
        return _pySmartIdEngine.MatchResultVector_get_allocator(self)

    def pop_back(self):
        return _pySmartIdEngine.MatchResultVector_pop_back(self)

    def erase(self, *args):
        return _pySmartIdEngine.MatchResultVector_erase(self, *args)

    def __init__(self, *args):
        this = _pySmartIdEngine.new_MatchResultVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _pySmartIdEngine.MatchResultVector_push_back(self, x)

    def front(self):
        return _pySmartIdEngine.MatchResultVector_front(self)

    def back(self):
        return _pySmartIdEngine.MatchResultVector_back(self)

    def assign(self, n, x):
        return _pySmartIdEngine.MatchResultVector_assign(self, n, x)

    def resize(self, *args):
        return _pySmartIdEngine.MatchResultVector_resize(self, *args)

    def insert(self, *args):
        return _pySmartIdEngine.MatchResultVector_insert(self, *args)

    def reserve(self, n):
        return _pySmartIdEngine.MatchResultVector_reserve(self, n)

    def capacity(self):
        return _pySmartIdEngine.MatchResultVector_capacity(self)
    __swig_destroy__ = _pySmartIdEngine.delete_MatchResultVector
    __del__ = lambda self: None
MatchResultVector_swigregister = _pySmartIdEngine.MatchResultVector_swigregister
MatchResultVector_swigregister(MatchResultVector)

class SegmentationResultVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SegmentationResultVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SegmentationResultVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pySmartIdEngine.SegmentationResultVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pySmartIdEngine.SegmentationResultVector___nonzero__(self)

    def __bool__(self):
        return _pySmartIdEngine.SegmentationResultVector___bool__(self)

    def __len__(self):
        return _pySmartIdEngine.SegmentationResultVector___len__(self)

    def __getslice__(self, i, j):
        return _pySmartIdEngine.SegmentationResultVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pySmartIdEngine.SegmentationResultVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pySmartIdEngine.SegmentationResultVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pySmartIdEngine.SegmentationResultVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pySmartIdEngine.SegmentationResultVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pySmartIdEngine.SegmentationResultVector___setitem__(self, *args)

    def pop(self):
        return _pySmartIdEngine.SegmentationResultVector_pop(self)

    def append(self, x):
        return _pySmartIdEngine.SegmentationResultVector_append(self, x)

    def empty(self):
        return _pySmartIdEngine.SegmentationResultVector_empty(self)

    def size(self):
        return _pySmartIdEngine.SegmentationResultVector_size(self)

    def swap(self, v):
        return _pySmartIdEngine.SegmentationResultVector_swap(self, v)

    def begin(self):
        return _pySmartIdEngine.SegmentationResultVector_begin(self)

    def end(self):
        return _pySmartIdEngine.SegmentationResultVector_end(self)

    def rbegin(self):
        return _pySmartIdEngine.SegmentationResultVector_rbegin(self)

    def rend(self):
        return _pySmartIdEngine.SegmentationResultVector_rend(self)

    def clear(self):
        return _pySmartIdEngine.SegmentationResultVector_clear(self)

    def get_allocator(self):
        return _pySmartIdEngine.SegmentationResultVector_get_allocator(self)

    def pop_back(self):
        return _pySmartIdEngine.SegmentationResultVector_pop_back(self)

    def erase(self, *args):
        return _pySmartIdEngine.SegmentationResultVector_erase(self, *args)

    def __init__(self, *args):
        this = _pySmartIdEngine.new_SegmentationResultVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _pySmartIdEngine.SegmentationResultVector_push_back(self, x)

    def front(self):
        return _pySmartIdEngine.SegmentationResultVector_front(self)

    def back(self):
        return _pySmartIdEngine.SegmentationResultVector_back(self)

    def assign(self, n, x):
        return _pySmartIdEngine.SegmentationResultVector_assign(self, n, x)

    def resize(self, *args):
        return _pySmartIdEngine.SegmentationResultVector_resize(self, *args)

    def insert(self, *args):
        return _pySmartIdEngine.SegmentationResultVector_insert(self, *args)

    def reserve(self, n):
        return _pySmartIdEngine.SegmentationResultVector_reserve(self, n)

    def capacity(self):
        return _pySmartIdEngine.SegmentationResultVector_capacity(self)
    __swig_destroy__ = _pySmartIdEngine.delete_SegmentationResultVector
    __del__ = lambda self: None
SegmentationResultVector_swigregister = _pySmartIdEngine.SegmentationResultVector_swigregister
SegmentationResultVector_swigregister(SegmentationResultVector)

class StringVectorCollection(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVectorCollection, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVectorCollection, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pySmartIdEngine.StringVectorCollection_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pySmartIdEngine.StringVectorCollection___nonzero__(self)

    def __bool__(self):
        return _pySmartIdEngine.StringVectorCollection___bool__(self)

    def __len__(self):
        return _pySmartIdEngine.StringVectorCollection___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _pySmartIdEngine.StringVectorCollection___getitem__(self, key)

    def __delitem__(self, key):
        return _pySmartIdEngine.StringVectorCollection___delitem__(self, key)

    def has_key(self, key):
        return _pySmartIdEngine.StringVectorCollection_has_key(self, key)

    def keys(self):
        return _pySmartIdEngine.StringVectorCollection_keys(self)

    def values(self):
        return _pySmartIdEngine.StringVectorCollection_values(self)

    def items(self):
        return _pySmartIdEngine.StringVectorCollection_items(self)

    def __contains__(self, key):
        return _pySmartIdEngine.StringVectorCollection___contains__(self, key)

    def key_iterator(self):
        return _pySmartIdEngine.StringVectorCollection_key_iterator(self)

    def value_iterator(self):
        return _pySmartIdEngine.StringVectorCollection_value_iterator(self)

    def __setitem__(self, *args):
        return _pySmartIdEngine.StringVectorCollection___setitem__(self, *args)

    def asdict(self):
        return _pySmartIdEngine.StringVectorCollection_asdict(self)

    def __init__(self, *args):
        this = _pySmartIdEngine.new_StringVectorCollection(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def empty(self):
        return _pySmartIdEngine.StringVectorCollection_empty(self)

    def size(self):
        return _pySmartIdEngine.StringVectorCollection_size(self)

    def swap(self, v):
        return _pySmartIdEngine.StringVectorCollection_swap(self, v)

    def begin(self):
        return _pySmartIdEngine.StringVectorCollection_begin(self)

    def end(self):
        return _pySmartIdEngine.StringVectorCollection_end(self)

    def rbegin(self):
        return _pySmartIdEngine.StringVectorCollection_rbegin(self)

    def rend(self):
        return _pySmartIdEngine.StringVectorCollection_rend(self)

    def clear(self):
        return _pySmartIdEngine.StringVectorCollection_clear(self)

    def get_allocator(self):
        return _pySmartIdEngine.StringVectorCollection_get_allocator(self)

    def count(self, x):
        return _pySmartIdEngine.StringVectorCollection_count(self, x)

    def erase(self, *args):
        return _pySmartIdEngine.StringVectorCollection_erase(self, *args)

    def find(self, x):
        return _pySmartIdEngine.StringVectorCollection_find(self, x)

    def lower_bound(self, x):
        return _pySmartIdEngine.StringVectorCollection_lower_bound(self, x)

    def upper_bound(self, x):
        return _pySmartIdEngine.StringVectorCollection_upper_bound(self, x)
    __swig_destroy__ = _pySmartIdEngine.delete_StringVectorCollection
    __del__ = lambda self: None
StringVectorCollection_swigregister = _pySmartIdEngine.StringVectorCollection_swigregister
StringVectorCollection_swigregister(StringVectorCollection)

class ImageFieldCollection(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ImageFieldCollection, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ImageFieldCollection, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pySmartIdEngine.ImageFieldCollection_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pySmartIdEngine.ImageFieldCollection___nonzero__(self)

    def __bool__(self):
        return _pySmartIdEngine.ImageFieldCollection___bool__(self)

    def __len__(self):
        return _pySmartIdEngine.ImageFieldCollection___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _pySmartIdEngine.ImageFieldCollection___getitem__(self, key)

    def __delitem__(self, key):
        return _pySmartIdEngine.ImageFieldCollection___delitem__(self, key)

    def has_key(self, key):
        return _pySmartIdEngine.ImageFieldCollection_has_key(self, key)

    def keys(self):
        return _pySmartIdEngine.ImageFieldCollection_keys(self)

    def values(self):
        return _pySmartIdEngine.ImageFieldCollection_values(self)

    def items(self):
        return _pySmartIdEngine.ImageFieldCollection_items(self)

    def __contains__(self, key):
        return _pySmartIdEngine.ImageFieldCollection___contains__(self, key)

    def key_iterator(self):
        return _pySmartIdEngine.ImageFieldCollection_key_iterator(self)

    def value_iterator(self):
        return _pySmartIdEngine.ImageFieldCollection_value_iterator(self)

    def __setitem__(self, *args):
        return _pySmartIdEngine.ImageFieldCollection___setitem__(self, *args)

    def asdict(self):
        return _pySmartIdEngine.ImageFieldCollection_asdict(self)

    def __init__(self, *args):
        this = _pySmartIdEngine.new_ImageFieldCollection(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def empty(self):
        return _pySmartIdEngine.ImageFieldCollection_empty(self)

    def size(self):
        return _pySmartIdEngine.ImageFieldCollection_size(self)

    def swap(self, v):
        return _pySmartIdEngine.ImageFieldCollection_swap(self, v)

    def begin(self):
        return _pySmartIdEngine.ImageFieldCollection_begin(self)

    def end(self):
        return _pySmartIdEngine.ImageFieldCollection_end(self)

    def rbegin(self):
        return _pySmartIdEngine.ImageFieldCollection_rbegin(self)

    def rend(self):
        return _pySmartIdEngine.ImageFieldCollection_rend(self)

    def clear(self):
        return _pySmartIdEngine.ImageFieldCollection_clear(self)

    def get_allocator(self):
        return _pySmartIdEngine.ImageFieldCollection_get_allocator(self)

    def count(self, x):
        return _pySmartIdEngine.ImageFieldCollection_count(self, x)

    def erase(self, *args):
        return _pySmartIdEngine.ImageFieldCollection_erase(self, *args)

    def find(self, x):
        return _pySmartIdEngine.ImageFieldCollection_find(self, x)

    def lower_bound(self, x):
        return _pySmartIdEngine.ImageFieldCollection_lower_bound(self, x)

    def upper_bound(self, x):
        return _pySmartIdEngine.ImageFieldCollection_upper_bound(self, x)
    __swig_destroy__ = _pySmartIdEngine.delete_ImageFieldCollection
    __del__ = lambda self: None
ImageFieldCollection_swigregister = _pySmartIdEngine.ImageFieldCollection_swigregister
ImageFieldCollection_swigregister(ImageFieldCollection)

class StringFieldCollection(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringFieldCollection, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringFieldCollection, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pySmartIdEngine.StringFieldCollection_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pySmartIdEngine.StringFieldCollection___nonzero__(self)

    def __bool__(self):
        return _pySmartIdEngine.StringFieldCollection___bool__(self)

    def __len__(self):
        return _pySmartIdEngine.StringFieldCollection___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _pySmartIdEngine.StringFieldCollection___getitem__(self, key)

    def __delitem__(self, key):
        return _pySmartIdEngine.StringFieldCollection___delitem__(self, key)

    def has_key(self, key):
        return _pySmartIdEngine.StringFieldCollection_has_key(self, key)

    def keys(self):
        return _pySmartIdEngine.StringFieldCollection_keys(self)

    def values(self):
        return _pySmartIdEngine.StringFieldCollection_values(self)

    def items(self):
        return _pySmartIdEngine.StringFieldCollection_items(self)

    def __contains__(self, key):
        return _pySmartIdEngine.StringFieldCollection___contains__(self, key)

    def key_iterator(self):
        return _pySmartIdEngine.StringFieldCollection_key_iterator(self)

    def value_iterator(self):
        return _pySmartIdEngine.StringFieldCollection_value_iterator(self)

    def __setitem__(self, *args):
        return _pySmartIdEngine.StringFieldCollection___setitem__(self, *args)

    def asdict(self):
        return _pySmartIdEngine.StringFieldCollection_asdict(self)

    def __init__(self, *args):
        this = _pySmartIdEngine.new_StringFieldCollection(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def empty(self):
        return _pySmartIdEngine.StringFieldCollection_empty(self)

    def size(self):
        return _pySmartIdEngine.StringFieldCollection_size(self)

    def swap(self, v):
        return _pySmartIdEngine.StringFieldCollection_swap(self, v)

    def begin(self):
        return _pySmartIdEngine.StringFieldCollection_begin(self)

    def end(self):
        return _pySmartIdEngine.StringFieldCollection_end(self)

    def rbegin(self):
        return _pySmartIdEngine.StringFieldCollection_rbegin(self)

    def rend(self):
        return _pySmartIdEngine.StringFieldCollection_rend(self)

    def clear(self):
        return _pySmartIdEngine.StringFieldCollection_clear(self)

    def get_allocator(self):
        return _pySmartIdEngine.StringFieldCollection_get_allocator(self)

    def count(self, x):
        return _pySmartIdEngine.StringFieldCollection_count(self, x)

    def erase(self, *args):
        return _pySmartIdEngine.StringFieldCollection_erase(self, *args)

    def find(self, x):
        return _pySmartIdEngine.StringFieldCollection_find(self, x)

    def lower_bound(self, x):
        return _pySmartIdEngine.StringFieldCollection_lower_bound(self, x)

    def upper_bound(self, x):
        return _pySmartIdEngine.StringFieldCollection_upper_bound(self, x)
    __swig_destroy__ = _pySmartIdEngine.delete_StringFieldCollection
    __del__ = lambda self: None
StringFieldCollection_swigregister = _pySmartIdEngine.StringFieldCollection_swigregister
StringFieldCollection_swigregister(StringFieldCollection)

class QuadrangleCollection(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, QuadrangleCollection, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, QuadrangleCollection, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pySmartIdEngine.QuadrangleCollection_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pySmartIdEngine.QuadrangleCollection___nonzero__(self)

    def __bool__(self):
        return _pySmartIdEngine.QuadrangleCollection___bool__(self)

    def __len__(self):
        return _pySmartIdEngine.QuadrangleCollection___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _pySmartIdEngine.QuadrangleCollection___getitem__(self, key)

    def __delitem__(self, key):
        return _pySmartIdEngine.QuadrangleCollection___delitem__(self, key)

    def has_key(self, key):
        return _pySmartIdEngine.QuadrangleCollection_has_key(self, key)

    def keys(self):
        return _pySmartIdEngine.QuadrangleCollection_keys(self)

    def values(self):
        return _pySmartIdEngine.QuadrangleCollection_values(self)

    def items(self):
        return _pySmartIdEngine.QuadrangleCollection_items(self)

    def __contains__(self, key):
        return _pySmartIdEngine.QuadrangleCollection___contains__(self, key)

    def key_iterator(self):
        return _pySmartIdEngine.QuadrangleCollection_key_iterator(self)

    def value_iterator(self):
        return _pySmartIdEngine.QuadrangleCollection_value_iterator(self)

    def __setitem__(self, *args):
        return _pySmartIdEngine.QuadrangleCollection___setitem__(self, *args)

    def asdict(self):
        return _pySmartIdEngine.QuadrangleCollection_asdict(self)

    def __init__(self, *args):
        this = _pySmartIdEngine.new_QuadrangleCollection(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def empty(self):
        return _pySmartIdEngine.QuadrangleCollection_empty(self)

    def size(self):
        return _pySmartIdEngine.QuadrangleCollection_size(self)

    def swap(self, v):
        return _pySmartIdEngine.QuadrangleCollection_swap(self, v)

    def begin(self):
        return _pySmartIdEngine.QuadrangleCollection_begin(self)

    def end(self):
        return _pySmartIdEngine.QuadrangleCollection_end(self)

    def rbegin(self):
        return _pySmartIdEngine.QuadrangleCollection_rbegin(self)

    def rend(self):
        return _pySmartIdEngine.QuadrangleCollection_rend(self)

    def clear(self):
        return _pySmartIdEngine.QuadrangleCollection_clear(self)

    def get_allocator(self):
        return _pySmartIdEngine.QuadrangleCollection_get_allocator(self)

    def count(self, x):
        return _pySmartIdEngine.QuadrangleCollection_count(self, x)

    def erase(self, *args):
        return _pySmartIdEngine.QuadrangleCollection_erase(self, *args)

    def find(self, x):
        return _pySmartIdEngine.QuadrangleCollection_find(self, x)

    def lower_bound(self, x):
        return _pySmartIdEngine.QuadrangleCollection_lower_bound(self, x)

    def upper_bound(self, x):
        return _pySmartIdEngine.QuadrangleCollection_upper_bound(self, x)
    __swig_destroy__ = _pySmartIdEngine.delete_QuadrangleCollection
    __del__ = lambda self: None
QuadrangleCollection_swigregister = _pySmartIdEngine.QuadrangleCollection_swigregister
QuadrangleCollection_swigregister(QuadrangleCollection)

# This file is compatible with both classic and new-style classes.


