from pathlib import Path


def alchemy_organize(path: str) -> None:
    directory = Path(path)

    audios_dir = directory / 'audios'
    images_dir = directory / 'images'
    docs_dir = directory / 'documents'
    videos_dir = directory / 'videos'
    others_dir = directory / 'others'

    AUDIOS_EXT = ['.mp3', '.wav', '.flac']  
    VIDEOS_EXT = ['.mp4', '.avi', '.mkv']   
    IMAGES_EXT = ['.jpg', '.png', '.gif']   
    DOCUMENTS_EXT = ['.pdf', '.docx', '.txt']  

    file_names = [f for f in directory.iterdir() if f.is_file()]

    for folder in [audios_dir, images_dir, docs_dir, videos_dir, others_dir]:
        folder.mkdir(exist_ok=True)

    for file in file_names:
        extension = Path(file).suffix.lower()

        if extension in AUDIOS_EXT:
            new_folder = audios_dir
        elif extension in VIDEOS_EXT:
            new_folder = videos_dir
        elif extension in IMAGES_EXT:
            new_folder = images_dir
        elif extension in DOCUMENTS_EXT:
            new_folder = docs_dir
        else:
            new_folder = others_dir
        
        new_path = new_folder / file.name
        
        file.rename(new_path)


if __name__ == '__main__':
    path = input(r'PATH: ')
    alchemy_organize(path)