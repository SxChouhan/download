import os
from pytube import Playlist
import subprocess
from multiprocessing import Pool


# Function to download a single Youtube video.
def download_single_video():
    # URL of the YouTube video you want to download
    video_url = input("Enter the video url: ")
    
    # Command to download the  video in mp4 format using yt-dlp
    command = ['yt-dlp', '-f', 'mp4','-o',f'C:\\Users\\admin\\Desktop\\down_videos\\%(title)s.%(ext)s', video_url]

    # Execute the command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Output the result
    print(result.stdout)
    print(result.stderr)




# Functin to download whole playlist at once woth multiprocessing.
def down_videos(command):
        # Execute the command in multi-processing
        return subprocess.run(command, check=True)


# Functin to download whole playlist at once.
def download_playlist():

    # Function to get playlist name uing pytube.
    def get_playlist_name(playlist_url):
        # Create a Playlist object
        playlist = Playlist(playlist_url)
        
        # Return the title of the playlist
        return playlist.title


    # Function to fetch video URLs from a playlist
    def fetch_video_urls(playlist_url):
        playlist = Playlist(playlist_url)
        video_urls = []
        for video in playlist.videos:
            video_urls.append(video.watch_url)
        return video_urls

    
    # Get playlis url from user.
    playlist_url = "https://www.youtube.com/watch?v=3jEw_atbO5M&list=PLj5GWDBCMHnZ1XApnYCAPz874rWmrlodT&pp=gAQBiAQB"
    # Fetch the playlist name.
    playlist_name = get_playlist_name(playlist_url)
    # Specify the downloaded video file path
    download_path = f'C:\\Users\\admin\\Desktop\\down_videos\\%s' % playlist_name

    
    # Ensure the download path exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    def every_command():
        # Calling the get url of playlist function
        playlist_urls = fetch_video_urls(playlist_url)
        commands_in = []
        for url in playlist_urls:
            # Build the yt-dlp command
            command = [
                'yt-dlp',
                '-o', os.path.join(download_path, '%(title)s.%(ext)s'),
                '-f','mp4',
                url
            ]
            commands_in.append(command)
        return commands_in
    
    


    commands = every_command()
    print(commands)
    print(len(commands))

    #for command in commands:
        #print(down_videos(command))

    try :
        with Pool(processes=len(commands)) as pool:
            pool.map(down_videos, commands)

    except:
        RuntimeError




# This function is left to complete.
def download_many_videos():
    # URL of the YouTube video you want to download
    video_url = input("Enter the video url: ")
    
    # Command to download the best quality video using yt-dlp
    command = ['yt-dlp', '-f', 'b','-o',f'C:\\Users\\admin\\Desktop\\down_videos\\%(title)s.%(ext)s', video_url]

    # Execute the command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Output the result
    print(result.stdout)
    print(result.stderr)





def main():

    print("1.Download single Youtube video \n2.Download Youtube playlist \n3.Download many Youtube videos")
    number = int(input("Enter the number: "))

    if number==1:
        # To download a single video
        download_single_video()

    elif number==2:
        # To downlod whole playlist
        download_playlist()

    else:
        # To download many videos
        download_many_videos()


if __name__ == "__main__":
    main()
