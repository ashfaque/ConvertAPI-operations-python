# https://shravan-c.medium.com/file-type-conversion-using-python-15961ed729c1

# https://anyconv.com/api/action/add/ec6cb3ed53bbdf14d9e8aab6c5721afb/ POST
#     file: (binary)
#     to: pdf
# https://anyconv.com/api/action/status/ec6cb3ed53bbdf14d9e8aab6c5721afb/ GET
#     {"status":false}
#     {"status":true,"url":"https:\/\/anyconv.com\/api\/action\/download\/ec6cb3ed53bbdf14d9e8aab6c5721afb\/","size":12645411}
# https://anyconv.com/api/action/download/ec6cb3ed53bbdf14d9e8aab6c5721afb/?name=PPT-56-Months.Eng%201st-Feb_2019RevisedLR.pdf  GET


if __name__ == "__main__":
    import os
    try:
        from dotenv import load_dotenv
        from global_function import get_execution_start_time, get_execution_end_time

        load_dotenv()
        start = get_execution_start_time()



        # ? docx to pdf -> f'{os.getcwd()}/test_files/demo.docx', f'{os.getcwd()}/output/demo.pdf'
        # RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
        # RUN apt-get install -y libreoffice
        # RUN apt-get install default-jre

        # def docx2pdfConvert(doc_file_path, pdf_folder_path):
        #     import subprocess
        #     args = ['libreoffice', '--headless', '--convert-to', 'pdf', doc_file_path, '--outdir', pdf_folder_path]
        #     success_flag = subprocess.run(args).returncode
        #     # output = subprocess.call(args)
        #     # output = subprocess.check_output(args)
        #     if success_flag == 0:    # ? A negative value -N indicates that the child was terminated by signal N. Aka, unsuccessful, https://docs.python.org/3/library/subprocess.html
        #         print('successful!')
        #     else: print('not successful')

        # docx2pdfConvert(f'{os.getcwd()}/test_files/demo.docx', f'{os.getcwd()}/output/')



        # ? jpeg to pdf -> f'{os.getcwd()}/test_files/Large Sample-Image-download-for-Testing.jpeg'
        from img2pdf import convert as img2pdfConvert
        # with open(f'{os.getcwd()}/output/Large Sample-Image-download-for-Testing.pdf', 'wb') as newPdfFile:
        #     newPdfFile.write(img2pdfConvert(f'{os.getcwd()}/test_files/Large Sample-Image-download-for-Testing.jpeg'))



        # ? jpg to pdf -> f'{os.getcwd()}/test_files/Large-Sample-Image-download-for Testing.jpg'
        from img2pdf import convert as img2pdfConvert
        # with open(f'{os.getcwd()}/output/Large-Sample-Image-download-for Testing.pdf', 'wb') as newPdfFile:
        #         newPdfFile.write(img2pdfConvert(f'{os.getcwd()}/test_files/Large-Sample-Image-download-for Testing.jpg'))



        # ? pptx to pdf -> f'{os.getcwd()}/test_files/PPT-56-Months.Eng 1st-Feb_2019RevisedLR.pptx'
        # RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
        # RUN apt-get install -y libreoffice
        # RUN apt-get install default-jre

        # def pptx2pdfConvert(ppt_file_path, pdf_folder_path):
        #     import subprocess
        #     args = ['libreoffice', '--headless', '--convert-to', 'pdf', ppt_file_path, '--outdir', pdf_folder_path]
        #     success_flag = subprocess.run(args).returncode
        #     # output = subprocess.call(args)
        #     # output = subprocess.check_output(args)
        #     if success_flag == 0:    # ? A negative value -N indicates that the child was terminated by signal N. Aka, unsuccessful, https://docs.python.org/3/library/subprocess.html
        #         print('successful!')
        #     else: print('not successful')

        # pptx2pdfConvert(f'{os.getcwd()}/test_files/PPT-56-Months.Eng 1st-Feb_2019RevisedLR.pptx', f'{os.getcwd()}/output/')



        # TODO: (1/2) dwg to pdf -> f'{os.getcwd()}/test_files/prague contour lines.dwg'
        # https://shravan-c.medium.com/file-type-conversion-using-python-15961ed729c1
        # https://github.com/vector-express/vectorexpress-api#cad2pdf



        # ? bmp to pdf -> f'{os.getcwd()}/test_files/sample 5184x3456.bmp'
        from PIL import Image
        # img = Image.open(f'{os.getcwd()}/test_files/sample 5184x3456.bmp')
        # img.save(f'{os.getcwd()}/output/sample 5184x3456.pdf','pdf')



        # ? doc to pdf -> f'{os.getcwd()}/test_files/SampleDOCFile 5000kb.doc'
        # RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
        # RUN apt-get install -y libreoffice
        # RUN apt-get install default-jre

        # def doc2pdfConvert(doc_file_path, pdf_folder_path):
        #     import subprocess
        #     args = ['libreoffice', '--headless', '--convert-to', 'pdf', doc_file_path, '--outdir', pdf_folder_path]
        #     success_flag = subprocess.run(args).returncode
        #     # output = subprocess.call(args)
        #     # output = subprocess.check_output(args)
        #     if success_flag == 0:    # ? A negative value -N indicates that the child was terminated by signal N. Aka, unsuccessful, https://docs.python.org/3/library/subprocess.html
        #         print('successful!')
        #     else: print('not successful')

        # doc2pdfConvert(f'{os.getcwd()}/test_files/SampleDOCFile 5000kb.doc', f'{os.getcwd()}/output/')



        # ? png to pdf -> f'{os.getcwd()}/test_files/SamplePNGImage 30mb.png'
        from img2pdf import convert as img2pdfConvert
        # with open(f'{os.getcwd()}/output/SamplePNGImage 30mb.pdf', 'wb') as newPdfFile:
        #         newPdfFile.write(img2pdfConvert(f'{os.getcwd()}/test_files/SamplePNGImage 30mb.png'))



        # ? ppt to pdf -> f'{os.getcwd()}/test_files/SamplePPTFile 1000kb.ppt'
        # RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
        # RUN apt-get install -y libreoffice
        # RUN apt-get install default-jre

        # def ppt2pdfConvert(ppt_file_path, pdf_folder_path):
        #     import subprocess
        #     args = ['libreoffice', '--headless', '--convert-to', 'pdf', ppt_file_path, '--outdir', pdf_folder_path]
        #     success_flag = subprocess.run(args).returncode
        #     # output = subprocess.call(args)
        #     # output = subprocess.check_output(args)
        #     if success_flag == 0:    # ? A negative value -N indicates that the child was terminated by signal N. Aka, unsuccessful, https://docs.python.org/3/library/subprocess.html
        #         print('successful!')
        #     else: print('not successful')

        # ppt2pdfConvert(f'{os.getcwd()}/test_files/SamplePPTFile 1000kb.ppt', f'{os.getcwd()}/output/')



        # ? txt to pdf -> f'{os.getcwd()}/test_files/SampleTextFile 1000kb.txt'
        # https://stackoverflow.com/a/64877141/16377463
        import textwrap
        from fpdf import FPDF
        from math import ceil, floor

        def text_to_pdf(input_filename_path, output_filename_path):
            file = open(input_filename_path)
            text = file.read()
            file.close()

            a4_width_mm = 210
            pt_to_mm = 0.35
            fontsize_pt = 10
            fontsize_mm = fontsize_pt * pt_to_mm
            margin_bottom_mm = 10
            character_width_mm = 7 * pt_to_mm
            width_text = a4_width_mm / character_width_mm

            pdf = FPDF(orientation='P', unit='mm', format='A4')
            pdf.set_auto_page_break(True, margin=margin_bottom_mm)
            pdf.add_page()
            pdf.set_font(family='Courier', size=fontsize_pt)
            # pdf.set_font(family='Times', size=fontsize_pt)
            splitted = text.split('\n')

            for line in splitted:
                # lines = textwrap.wrap(line, ceil(width_text))
                lines = textwrap.wrap(line, floor(width_text))

                if len(lines) == 0:
                    pdf.ln()    # If a blank line exists then create an empty line

                for wrap in lines:
                    pdf.cell(0, fontsize_mm, wrap, ln=1)
                pdf.ln()    # Add empty line below each line

            pdf.output(output_filename_path, 'F')

        text_to_pdf(f'{os.getcwd()}/test_files/SampleTextFile 1000kb.txt', f'{os.getcwd()}/output/SampleTextFile 1000kb.pdf')



        # ? merging all output pdf to one pdf:-
        # https://stackoverflow.com/questions/3444645/merge-pdf-files
        from PyPDF2 import PdfFileMerger, PdfMerger
        # allpdfs = [
        #         f'{os.getcwd()}/test_files/[READ] Malvino_Electronic-Principles.pdf'
        #         , f'{os.getcwd()}/output/demo.pdf'
        #         , f'{os.getcwd()}/output/Large Sample-Image-download-for-Testing.pdf'
        #         , f'{os.getcwd()}/output/Large-Sample-Image-download-for Testing.pdf'
        #         , f'{os.getcwd()}/output/PPT-56-Months.Eng 1st-Feb_2019RevisedLR.pdf'
        #         # , f'{os.getcwd()}/output/prague contour lines.pdf'
        #         , f'{os.getcwd()}/output/sample 5184x3456.pdf'
        #         , f'{os.getcwd()}/output/SampleDOCFile 5000kb.pdf'
        #         , f'{os.getcwd()}/output/SamplePNGImage 30mb.pdf'
        #         , f'{os.getcwd()}/output/SamplePPTFile 1000kb.pdf'
        #         , f'{os.getcwd()}/output/SampleTextFile 1000kb.pdf'
        # ]
        # merger = PdfFileMerger()
        # # merger = PdfMerger()
        # [merger.append(pdf) for pdf in allpdfs]
        # with open(f'{os.getcwd()}/output/merged.pdf', 'wb') as newPdfFile:
        #     merger.write(newPdfFile)



        print('Total time taken::::: ', get_execution_end_time(start))

    except ModuleNotFoundError:
        os.system('python -m pip install --upgrade pip')
        os.system('pip install --no-cache-dir --upgrade python-dotenv')

        os.system('pip install --no-cache-dir --upgrade img2pdf')
        os.system('pip install --no-cache-dir --upgrade Pillow')
        os.system('pip install --no-cache-dir --upgrade fpdf')
        os.system('pip install --no-cache-dir --upgrade PyPDF2')
