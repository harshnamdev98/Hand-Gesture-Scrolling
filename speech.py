import random
import time
import speech_recognition as sr
import handy1

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitiviFalsety to ambient noise and record audio
    # from the microphone
    recognizer.dynamic_energy_threshold =True 
    with microphone as source:
        recognizer.energy_threshold=1500
        recognizer.pause_threshold=0.5
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


def speech_main():
    # if __name__ == "__main__":
    # set the list of words, maxnumber of guesses, and prompt limit
    # WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
    WORDS = ["zoom in","ZoomIn","zoom out","ZoomOut","Terminal","terminal"]
    NUM_GUESSES = 300
    PROMPT_LIMIT = 20

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # # get a random word from the list
    # word = random.choice(WORDS)

    # # format the instructions string
    # instructions = (
    #     "I'm thinking of one of these words:\n"
    #     "{words}\n"
    #     "You have {n} tries to guess which one.\n"
    # ).format(words=', '.join(WORDS), n=NUM_GUESSES)

    # show instructions and wait 3 seconds before starting the game
    # print(instructions)
    # time.sleep(2)


    for i in range(NUM_GUESSES):

        # get the guess from the user
        # if a transcription is returned, break out of the loop and
        #     continue
        # if no transcription returned and API request failed, break
        #     loop and continue
        # if API request succeeded but no transcription was returned,
        #     re-prompt the user to say their guess again. Do this up
        #     to PROMPT_LIMIT times
        for j in range(PROMPT_LIMIT):
            print('{}. Speak!'.format(i+1))
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. What did you say?\n")

        # if there was an error, stop the game
        # if guess["error"]:
        #     print("ERROR: {}".format(guess["error"]))
        #     break

        # show the user the transcription
        print("You said: {}".format(guess["transcription"]))
        if guess["transcription"]==None:
            continue
        # determine if guess is correct and if any attempts remain
        guess_is_correct = guess["transcription"].lower() 
        user_has_more_attempts = i < NUM_GUESSES - 1

        # determine if the user has won the game
        # if not, repeat the loop if user has more attempts
        # if no attempts left, the user loses the game
        print(guess_is_correct," this is comparanble")

        ##added 28-12-19
        if guess_is_correct.find('zoom in') != -1 or  guess_is_correct.find('zoomin') != -1:
            print("zoom in -100")
            handy1.action_func('zoomin')
        elif guess_is_correct.find('zoom out') != -1 or  guess_is_correct.find('zoomout') != -1:
            print ('zoom out +100')
            handy1.action_func('zoomout')
        elif guess_is_correct.find('terminal') != -1 or  guess_is_correct.find('cmd') != -1:
            print ('open terminal')
            handy1.action_func('terminal')
        elif guess_is_correct.find('close tab')!=-1 or guess_is_correct.find('closetab')!=-1:
            print('close tab')
            handy1.action_func('closetab')
        elif guess_is_correct.find('open tab')!=-1 or guess_is_correct.find('opentab')!=-1 or guess_is_correct.find('newtab')!=-1 or guess_is_correct.find('new tab')!=-1:
            print('open tab')
            handy1.action_func('opentab')
        elif guess_is_correct.find('close window')!=-1 or guess_is_correct.find('closewindow')!=-1:
            print('close window')
            handy1.action_func('closewindow')
        elif guess_is_correct.find('screenshot')!=-1 or guess_is_correct.find('screen shot')!=-1:
            print('screen shot')
            handy1.action_func('screenshot')
        
        

        # if guess_is_correct == 'zoom in' or guess_is_correct=="zoomin":
        #     print("zoom in -100")
        #     handy1.action_func('zoomin')
        #     # break
        # elif guess_is_correct == 'zoom out' or guess_is_correct=="zoomout":
        #     print ('zoom out +100')
        #     handy1.action_func('zoomout')
        # elif user_has_more_attempts:
        #     print("Incorrect. Try again.\n")
        # else:
        #     print("Sorry, you lose!\nI was thinking of '{}'.".format(word))
            # break

speech_main()
