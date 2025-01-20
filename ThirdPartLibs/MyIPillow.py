"""
The module is designed to convert files with images or .pdf to pdf format with the conversion of images to black
and white mode. Typically, such tasks arise when preparing scanned copies of documents for submission at the request
of government agencies or for standardization of electronic archive files.
"""

from PIL import Image, UnidentifiedImageError
# почему-то не установился pypdf, поэтому пришлось найти другую библиотеку для перекрашивания в ч\б pdf
# эта библиотека нужна потому что PIL не умеет открывать и обрабатывать pdf
import pymupdf
import os


def convert_pdf_to_bw(input_pdf: str, source_pdf: str) -> None:
    """
    The function converts the contents of a specific pdf file into a grayscale "image" mode. The pymupdf library is used
    :param input_pdf: path to .pdf file
    :param source_pdf: path (including file's name) to create new .pdf file in grayscale "image" mode.
    :return: nothing
    """
    doc = pymupdf.open(input_pdf)
    new_doc = pymupdf.open()
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(colorspace=pymupdf.csGRAY)
        new_page = new_doc.new_page(width=pix.width, height=pix.height)
        new_page.insert_image(new_page.rect, pixmap=pix)
    new_doc.save(source_pdf)
    new_doc.close()
    doc.close()


def convert_all_to_pdf_bw(path: str) -> None:
    """
    Function converts all files in current dir to .pdf format in grayscale mode.
    If exceptions occurs (f.e. non-image file's format, unknown format, other errors) file is moved to
    the folder "Exceptions" for manual processing. Successfully processed files are placed in the folder "Output"
    :param path: folder with files to process
    :return: Nothing
    """
    output_dir = 'Output'
    if not os.path.exists(fr'{path}\{output_dir}'):
        os.mkdir(fr'{path}\{output_dir}')
    exceptions_dir = 'Exceptions'
    if not os.path.exists(fr'{path}\{exceptions_dir}'):
        os.mkdir(fr'{path}\{exceptions_dir}')
    for file in os.listdir(path):
        file_fullpath = os.path.join(path, file)
        if os.path.isfile(file_fullpath):
            file_name, ext = os.path.splitext(file)
            try:
                with Image.open(file_fullpath) as source_file:
                    source_file = source_file.convert(mode='L')
                    source_file.save(fr'{path}\{output_dir}\{file_name}.pdf', save_all=True, optimize=True)
            except UnidentifiedImageError:
                if ext == '.pdf':
                    convert_pdf_to_bw(file_fullpath, fr'{path}\{output_dir}\{file}')
                else:
                    os.system(fr'copy {file_fullpath} {path}\{exceptions_dir}\{file}')


def main():
    convert_all_to_pdf_bw(
        r'C:\Users\Александр\PycharmProjects\PythonDeveloper---UrbanUnivercity\ThirdPartLibs\RawFiles')


main()
