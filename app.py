from tracks import SpotifyApi
import random


def main():
    CLIENT_ID = '0dcba0e2ef534d4b9e25752ef8c73393'
    CLIENT_SECRET = 'd99e595a25e64550bcd132a9eb7cdca8'
    api = SpotifyApi(CLIENT_ID, CLIENT_SECRET)

    playlist_id = '1nDlz26IVMKgtSZCDXgyn9?si=ae9576cfe01f4421'

    print("Click on link and guess the song or type 'exit' to finish the game")

    list_ids = api.get_id_music_in_playlist(playlist_id)

    music_right = 0
    artists_right = 0
    musics_right = 0
    music_points = 5
    artist_points = 2

    print("1 -> Easy, 2-> Hard")
    level = input()

    if level == '1':
        for track in list_ids:
            track_info = api.get_track_info(track)
            music_name = track_info.get_music_name()
            artist_name = track_info.get_artist_name()
            url = track_info.get_music_url()

            if url is None:
                continue
            print("What is the name of this music?")
            print(url)

            show_musics_to_choose = []

            for show_musics in range(3):
                track_info = api.get_track_info(random.choice(list_ids))
                choose_music_name = track_info.get_music_name()
                show_musics_to_choose.append(choose_music_name)

            show_musics_to_choose.append(music_name)
            random.shuffle(show_musics_to_choose)

            for show in show_musics_to_choose:
                print(show)

            print("Your answer is: ")
            answer = input()

            if answer == 'exit':
                break

            if answer.lower() == music_name.lower():
                print("Right :D")
                musics_right = musics_right + 1
                music_right = music_right + music_points
            else:
                print("The right answer is: " + music_name)

            print("Who is singing?")
            singer_answer = input()

            if singer_answer.lower() == artist_name.lower():
                print("Yes!")
                artists_right = artists_right + artist_points
            else:
                print("The correct answer is: " + artist_name)

    if level == '2':
        for track in list_ids:
            track_info = api.get_track_info(track)
            music_name = track_info.get_music_name()
            artist_name = track_info.get_artist_name()
            url = track_info.get_music_url()

            if url is None:
                continue
            print(url)

            print("What is the name of this music? (Type 'tip' to help you)")
            answer = input()

            if answer == 'exit':
                break

            if answer == 'tip':
                print(track_info.tip())
                print("What is the name of this music?")
                answer = input()

            if answer != 'tip':
                if answer.lower() == music_name.lower():
                    print("Right :D")
                    musics_right = musics_right + 1
                    music_right = music_right + music_points
                else:
                    print("The right answer is: " + music_name)

            print("Who is singing?")
            singer_answer = input()

            if singer_answer.lower() == artist_name.lower():
                print("Yes!")
                artists_right = artists_right + artist_points
            else:
                print("The correct answer is: " + artist_name)

    if musics_right <= 1:
        print("You're right " + str(musics_right) + " music")
    else:
        print("You're right " + str(music_right) + " musics")

    print("Artists you know " + str(artists_right))

    score = music_right + artists_right

    print("Your score: " + str(score))


if __name__ == '__main__':
    main()
