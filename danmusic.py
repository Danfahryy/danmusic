import vlc
import youtube_dl
import time
from colorama import Fore, Style, init
from pyfiglet import figlet_format

# Inisialisasi colorama
init(autoreset=True)

def play_music(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'temp_audio.%(ext)s',
        'noplaylist': True,
        'quiet': True
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        audio_url = info_dict['formats'][0]['url']

    player = vlc.MediaPlayer(audio_url)
    player.play()
    return player

def stop_music(player):
    player.stop()

def print_large_text(text, color):
    """Print text in a large font and specified color."""
    large_text = figlet_format(text, font="slant")  # Menggunakan font 'slant' dari pyfiglet
    print(color + large_text + Style.RESET_ALL)

def main():
    player = None
    while True:
        print_large_text("Danvertt", Fore.GREEN)  # Teks besar dengan warna hijau
        print("TOOLS SEDERHANA PEMUTAR MUSIC BY LINK YOUTUBE!")
        print("Menu:")
        print("1. Putar Musik")
        print("2. Stop Musik")
        print("3. Keluar")
        
        choice = input("Pilih opsi (1/2/3): ")
        
        if choice == '1':
            url = input("Masukkan link YouTube: ")
            if player and player.is_playing():
                stop_music(player)
            player = play_music(url)
            print("Musik sedang diputar...")
        
        elif choice == '2':
            if player and player.is_playing():
                stop_music(player)
                print("Musik dihentikan.")
            else:
                print("Tidak ada musik yang sedang diputar.")
        
        elif choice == '3':
            if player and player.is_playing():
                stop_music(player)
            print("Keluar dari program.")
            break
        
        else:
            print("Opsi tidak valid. Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":
    main()
