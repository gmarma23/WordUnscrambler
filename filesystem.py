from pathlib import Path

class Filesystem():
    __ROOT_DIR = Path(__file__).parent
    __DEFAULT_MAPPED_DIR = __ROOT_DIR / 'wordlists' / 'mapped'
    __DEFAULT_OUTPUT_PATH = __ROOT_DIR / 'output'


    @staticmethod
    def get_output_file_path(filename: str) -> Path:
        Filesystem.__DEFAULT_OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
        final_filename = Filesystem.__duplicate_items_handler(Filesystem.__DEFAULT_OUTPUT_PATH, filename)
        return Filesystem.__DEFAULT_OUTPUT_PATH / final_filename

    
    @staticmethod
    def get_mapped_wordlist_path(wordlist_filename: str) -> Path:
        Filesystem.__DEFAULT_MAPPED_DIR.mkdir(parents=True, exist_ok=True)
        return Filesystem.__DEFAULT_MAPPED_DIR / wordlist_filename
    

    @staticmethod
    def get_filename_stem(file_path :str) -> str:
        return str(Path(file_path).stem)
    

    @staticmethod
    def get_filename_suffix(file_path :str) -> str:
        return str(Path(file_path).suffix)
    

    @staticmethod
    def __duplicate_items_handler(dir_path: Path, init_filename: str) -> str:
        final_filename = init_filename
        stem = Filesystem.get_filename_stem(final_filename)
        suffix = Filesystem.get_filename_suffix(final_filename)
        index = 1

        while final_filename in dir_path.glob('**/*'):
            final_filename = f'{stem}_{str(index)}{suffix}'
            index += 1

        return final_filename
