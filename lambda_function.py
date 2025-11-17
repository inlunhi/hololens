# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import ui

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from ask_sdk_model.interfaces.alexa.presentation.apl import ( 
RenderDocumentDirective, ExecuteCommandsDirective, SpeakItemCommand, AutoPageCommand, HighlightMode)
import urllib.request

from utils import create_presigned_url

from PIL import Image

mainjson = {
    "type": "APL",
    "version": "1.7",
    "license": "Copyright 2021 Amazon.com, Inc. or its affiliates blah blah",
    "settings": {},
    "theme": "dark",
    "import": [],
    "resources": [],
    "styles": {},
    "onMount": [],
    "graphics": {},
    "commands": {},
    "layouts": {},
    "mainTemplate": {
        "parameters": [
            "payload"
        ],
        "items": [
            {
                "type": "Container",
                "items": [
                    {
                        "source": "imageurl",
                        "type": "Image",
                        "width": "100vw",
                        "height": "100vh"
                    }
                ]
            }
        ]
    }
}

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello, Welcome to the Nano Human Interfaces Initiative!"
        # I changed the pic url for testing
        urllib.request.urlretrieve('https://raw.githubusercontent.com/aabikshetri/NHI-Image/main/Hololens2.jp', "/tmp/Hololens1.png")
        imagegif= Image.open("/tmp/Hololens1.png")
        imagegif.save(r'/tmp/Hololens1.png')
        object_name = 'Hololens1.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens1.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )


class HololensIntroIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HololensIntroIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "A hololens is a self-contained holographic device with applications to increase user accuracy and output. For students, the Hololens2 improves learning results with hands-on lessons that convey complex concepts in 3D."
        urllib.request.urlretrieve('https://raw.githubusercontent.com/aabikshetri/NHI-Image/main/Hololens2.jpg', "/tmp/Hololens2.png")
        imagegif= Image.open("/tmp/Hololens2.png")
        imagegif.save(r'/tmp/Hololens2.png')
        object_name = 'Hololens2.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens2.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )


class HololensTurnOnIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HololensTurnOnIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "To turn on the Hololens, press the small, round black button on the back right hand side of the headset."
        urllib.request.urlretrieve('https://raw.githubusercontent.com/aabikshetri/NHI-Image/main/Hololens4.jpg', "/tmp/Hololens4.png")
        imagegif= Image.open("/tmp/Hololens4.png")
        imagegif.save(r'/tmp/Hololens4.png')
        object_name = 'Hololens4.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens4.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )

class AdjustHeadsetIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AdjustHeadsetIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "There is a large circular knob on the back of the headset that will allow you to adjust the headset for your head size"
        urllib.request.urlretrieve('https://raw.githubusercontent.com/aabikshetri/NHI-Image/main/Hololens3.jpg', "/tmp/Hololens3.png")
        imagegif= Image.open("/tmp/Hololens3.png")
        imagegif.save(r'/tmp/Hololens3.png')
        object_name = 'Hololens3.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens3.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )


class SelectItemHeadsetIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SelectItemHeadsetIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Use your index finger to point and select menu items."
        urllib.request.urlretrieve('https://raw.githubusercontent.com/aabikshetri/NHI-Image/main/Hololens6.jpg', "/tmp/Hololens6.png")
        imagegif= Image.open("/tmp/Hololens6.png")
        imagegif.save(r'/tmp/Hololens6.png')
        object_name = 'Hololens6.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens6.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Thank you for having me. I hope you had a good time. Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class GraspObjectIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GraspObjectIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "To grasp objects use your open and closed fingertips"
        urllib.request.urlretrieve('https://raw.githubusercontent.com/aabikshetri/NHI-Image/main/Hololens7.jpg', "/tmp/Hololens7.png")
        imagegif= Image.open("/tmp/Hololens7.png")
        imagegif.save(r'/tmp/Hololens7.png')
        object_name = 'Hololens7.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens7.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )

class returntohomescreenIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("returntohomescreenIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "To return to the home screen, tap your index and middle finger of your left hand on your right hand wrist"
        urllib.request.urlretrieve('https://raw.githubusercontent.com/aabikshetri/NHI-Image/main/Hololens8.jpg', "/tmp/Hololens8.png")
        imagegif= Image.open("/tmp/Hololens8.png")
        imagegif.save(r'/tmp/Hololens8.png')
        object_name = 'Hololens8.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens8.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )

class getmoreappsIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("getmoreappsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Scroll down using the arrows on the right hand side of your screen"
        urllib.request.urlretrieve('https://raw.githubusercontent.com/aabikshetri/NHI-Image/main/Hololens9.jpg', "/tmp/Hololens9.png")
        imagegif= Image.open("/tmp/Hololens9.png")
        imagegif.save(r'/tmp/Hololens9.png')
        object_name = 'Hololens9.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens9.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )

class grainboundryappdoIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("grainboundryappdoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The grain boundary app shows a crystalline structure that you may blow apart by saying, Explode to view the individual grains. Say return to go back."
        urllib.request.urlretrieve('https://raw.githubusercontent.com/aabikshetri/NHI-Image/main/Hololens10.jpg', "/tmp/Hololens10.png")
        imagegif= Image.open("/tmp/Hololens10.png")
        imagegif.save(r'/tmp/Hololens10.png')
        object_name = 'Hololens10.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens10.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )

class grainboundryappaboutIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("grainboundryappaboutIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Click the narration option to hear more details about the Grain Boundary app"
        urllib.request.urlretrieve('https://raw.githubusercontent.com/aabikshetri/NHI-Image/main/Hololens11.jpg', "/tmp/Hololens11.png")
        imagegif= Image.open("/tmp/Hololens11.png")
        imagegif.save(r'/tmp/Hololens11.png')
        object_name = 'Hololens11.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens11.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )

class isgrainboundryapptolargeforscreenIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("isgrainboundryapptolargeforscreenIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "If the 3D crystal is too large for the headset screen, say, Shrink"
        urllib.request.urlretrieve('https://raw.githubusercontent.com/aabikshetri/NHI-Image/main/Hololens12.jpg', "/tmp/Hololens12.png")
        imagegif= Image.open("/tmp/Hololens12.png")
        imagegif.save(r'/tmp/Hololens12.png')
        object_name = 'Hololens12.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens12.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )

class whatifcarbonnanotubeistolargeIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("whatifcarbonnanotubeistolargeIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "If the nanotube is too large for the screen, you may say, Shrink to reduce the size. "
        
        return (
            handler_input.response_builder
               .speak(speak_output)
               .response
        )

class carbonnanotubeisaboutIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("carbonnanotubeisaboutIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Click the narration option to hear more details about the DNA wrapped carbon nanotube app."
        urllib.request.urlretrieve('https://raw.githubusercontent.com/aabikshetri/NHI-Image/main/Hololens13.jpg', "/tmp/Hololens13.png")
        imagegif= Image.open("/tmp/Hololens13.png")
        imagegif.save(r'/tmp/Hololens13.png')
        object_name = 'Hololens13.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens13.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )

class whatprotinscaffoldappdoIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("whatprotinscaffoldappdoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The Cell Scaffold app simulates what happens when a peptide attached to the cell scaffold, beneficially assuming its properties."
        urllib.request.urlretrieve('https://raw.githubusercontent.com/inlunhi/HololenPictures/main/HeadSetBuddy_CellScaffold.jpeg', "/tmp/Hololens14.png")
        imagegif= Image.open("/tmp/Hololens14.png")
        imagegif.save(r'/tmp/Hololens14.png')
        object_name = 'Hololens14.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens14.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )

class programusedtomakehololensappsIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("programusedtomakehololensappsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Our Hololens apps are programmed in C# using Unity as the Game Engine. Some people also use Unreal Engine."
        urllib.request.urlretrieve('https://raw.githubusercontent.com/aabikshetri/NHI-Image/main/Hololens15.jpg', "/tmp/Hololens15.png")
        imagegif= Image.open("/tmp/Hololens15.png")
        imagegif.save(r'/tmp/Hololens15.png')
        object_name = 'Hololens15.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens15.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )

class AdjustBrightnessIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AdjustBrightnessIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Turn up the brightness by pressing the button on the front left of the headset."
        urllib.request.urlretrieve('https://raw.githubusercontent.com/aabikshetri/NHI-Image/main/Hololens5.jpg', "/tmp/Hololens5.png")
        imagegif= Image.open("/tmp/Hololens5.png")
        imagegif.save(r'/tmp/Hololens5.png')
        object_name = 'Hololens5.png'
        image_url, s3_client, bucket_name = create_presigned_url(object_name)
        s3_client.upload_file(Filename='/tmp/Hololens5.png', Bucket=bucket_name, Key=object_name)
        mainjson["mainTemplate"]["items"][0]["items"][0]["source"] = image_url
        return (
                handler_input.response_builder
                .speak(speak_output)
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=mainjson
                    )
                )
                .response
            )

class aboutprotinscaffoldappIntentHandler(AbstractRequestHandler):
    """Handler for Lehigh Buddy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("aboutprotinscaffoldappIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Click the narration option to hear more details about the cell Scaffold app."
        
        return (
            handler_input.response_builder
               .speak(speak_output)
               .response
        )

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HololensIntroIntentHandler())
sb.add_request_handler(HololensTurnOnIntentHandler())
sb.add_request_handler(AdjustHeadsetIntentHandler())
sb.add_request_handler(SelectItemHeadsetIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(GraspObjectIntentHandler())
sb.add_request_handler(returntohomescreenIntentHandler())
sb.add_request_handler(getmoreappsIntentHandler())
sb.add_request_handler(grainboundryappdoIntentHandler())
sb.add_request_handler(grainboundryappaboutIntentHandler())
sb.add_request_handler(isgrainboundryapptolargeforscreenIntentHandler())
sb.add_request_handler(whatifcarbonnanotubeistolargeIntentHandler())
sb.add_request_handler(carbonnanotubeisaboutIntentHandler())
sb.add_request_handler(whatprotinscaffoldappdoIntentHandler())
sb.add_request_handler(programusedtomakehololensappsIntentHandler())
sb.add_request_handler(aboutprotinscaffoldappIntentHandler())
sb.add_request_handler(AdjustBrightnessIntentHandler())


sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
