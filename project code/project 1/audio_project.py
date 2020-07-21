"""
CS101 Audio Project Example
Gwen Urbanczyk
"""


from cs101audio import *

def reverse_audio(audio):
    """
    Reverses an Audio object's audio
    
    Arguments
    audio -- The audio object to be reversed
    """
    result = Audio()
    result_samples = result.get_sample_list()
    sample_lst = audio.get_sample_list()
    for index in range((len(sample_lst) - 1), -1, -1):
        result_samples.append(sample_lst[index])

    result.from_sample_list(result_samples, template=audio)
    
    return result

def mix_up_aud(audio):
    """
    Mixes up the audio, by mixing sample list: Ex: [1, 2, 3, 4, 5, 6] becomes [1, 6, 2, 5, 3, 4]
    Hides the message better than just reversing.
    
    Arguments:
    audio -- The audio to be mixed up
    
    """
    result = Audio()
    result_samples = result.get_sample_list()
    sample_lst = audio.get_sample_list()
    
    for index in range(len(sample_lst) // 2):
        # append front half element in forward direction
        result_samples.append(sample_lst[index])
        # append back half element in reverse direction
        result_samples.append(sample_lst[len(sample_lst) - 1 - index])
    
    
    # Creates new audio using the metadata of template(audio)
    result.from_sample_list(result_samples, template=audio)
    
    return result
    
def demix_audio(audio):
    """
    Demixes the audio (reverses mix_up_aud())  [1, 6, 2, 5, 3, 4] becomes [1, 2, 3, 4, 5, 6]
    
    Arguments:
    audio -- The Audio Object to be demixed 
    """
    sample_lst = audio.get_sample_list()
    result_end = []
    result_start = []
    
    for index in range(len(sample_lst)):
        # if we have an even index, we have a front half element
        if index % 2 == 0:
            result_start.append(sample_lst[index])
        # otherwise, we have a back half element
        else:
            result_end.append(sample_lst[index])
    
    result = Audio()
    
    # We have the reverse the back half because they were appended in reverse order
    result.from_sample_list(result_start + result_end[::-1], template=audio)
    return result



def main():
    """
    Program creates song ('Voidfish Duet' by Griffin Mcelroy) using wave generators,
    imports a audio file of my voice to be a hidden message, then hides it inside
    the song. Hidden by slowing down the message so that it's length is equal to the song's
    and then using the mix_up_aud function on it to jumble up the audio so you can't hear it
    while the song is being played normally. demix_audio function is used in conjunction with a speedup
    to hear the hidden message
    
    You can also use reverse_audio instead of mix and demix, but I found that mix and demix work a bit
    better at hiding the message, and they're a bit more complicated, and I was a bit bored.
    """
    egg_type = "Sine"
    babe_type = "Sawtooth"
    egg_gain = 0
    babe_gain = -15
    quarter_dur = 250
    half_dur = quarter_dur * 2
    whole_dur = half_dur * 2


    # Note Creation For Bass
    e3_whole = generate_music_note('e3', whole_dur, egg_type, egg_gain)
    e3_whole_flat = generate_music_note('eb3', whole_dur, egg_type, egg_gain)
    
    g3_whole = generate_music_note('g3', whole_dur, egg_type, egg_gain)
    g3_wholesharp = generate_music_note('g#3', whole_dur, egg_type, egg_gain)
    g3_wholeflat = generate_music_note('gb3', whole_dur, egg_type, egg_gain)
    
    g3_halfdot_whole = generate_music_note('g3', whole_dur + int(half_dur * 1.5), \
                                           egg_type, egg_gain)
    g3_halfdot_whole_sharp = generate_music_note('g#3', whole_dur + int(half_dur * 1.5), \
                                                 egg_type, egg_gain)
    g3_halfdot_whole_flat = generate_music_note('gb3', whole_dur + int(half_dur * 1.5), \
                                                egg_type, egg_gain)
    
    # Note creation for melody
    b3 = generate_music_note('b3', quarter_dur, babe_type, babe_gain)
    a3 = generate_music_note('a3', quarter_dur, babe_type, babe_gain)
    ab3 = generate_music_note('ab3', quarter_dur, babe_type, babe_gain)
    g3 = generate_music_note('g3', quarter_dur, babe_type, babe_gain)
    gb3 = generate_music_note('gb3', quarter_dur, babe_type, babe_gain)
    e4 = generate_music_note('e4', quarter_dur, babe_type, babe_gain)
    
    

    # Putting the notes together
    # Audio(quater_dur) creates a silent segment for quarter_dur milliseconds
    egg = Audio(quarter_dur) + e3_whole + g3_whole + g3_halfdot_whole
    
    eggsharp = Audio(quarter_dur) + e3_whole + g3_wholesharp + g3_halfdot_whole_sharp
    eggflat = Audio(quarter_dur) + e3_whole_flat + g3_wholeflat + g3_halfdot_whole_flat
    
    babe = (b3 + a3 + b3 + e4)
    babe_flat = (b3 + ab3 + b3 + e4) * 4
    bgbe = (b3 + g3 + b3 + e4) * 4
    bgbe_flat = (b3 + gb3 + b3 + e4) * 4
    
    egg += eggsharp + egg + eggflat
    egg *= 2
    
    
    song = babe * 10
    song += babe_flat + babe * 4 + bgbe_flat + babe * 4 + babe_flat + bgbe + bgbe_flat
    
    # Overlaying the melody and the bass
    song.overlay(egg, position=6000)
    
    # Adding a fade to the end of the song
    song.fade_out(1000)

    hidden_msg = Audio()
    # Importing message to be hidden
    hidden_msg.open_audio_file('hidden_msg.wav')
    
    
    # Caluclating the slowdown factor needed to make the hidden_msg as long as the song
    # (I round to 4 decimal places, but it really just depends on how close you want it to be)
    slowdown = len(hidden_msg) / len(song)
    slowdown = round(slowdown, 4)
    hidden_msg.change_speed(slowdown)


    # Mix up the message
    hidden_msg = mix_up_aud(hidden_msg)
    
    # Combine the song and the message
    song.overlay(hidden_msg)
    
    # Play the song with the message hidden inside
    song.play()
    
    
    # Decode the message
    song.change_speed(round(1 / slowdown, 4))
    song = demix_audio(song)
    
    # It can be quite loud so I reduce the volume a bit
    song.apply_gain(-2)
    
    # Then play the message
    song.play()

if __name__ == "__main__":
    main()