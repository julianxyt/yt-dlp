$var = 'https://www.youtube.com/watch?v=mMfxI3r_LyA&ab_channel=ModjoOfficial'
$folder = 'D:\Music - HDD\Music Repository\2025 Club'
#No Playlist
yt-dlp -x --no-playlist --cookies cookies.txt -P $folder --audio-format mp3 $var

#Playlist
yt-dlp -x --yes-playlist --cookies cookies.txt --sleep-interval 10 -P 'D:\Music - HDD\Music Repository\2025 Club' --audio-format mp3 'https://www.youtube.com/playlist?list=OLAK5uy_nSIlyvjzWS-Y6sZb24dhzcg0UlQazxn5k'
