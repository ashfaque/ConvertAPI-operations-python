if __name__ == "__main__":
    import os
    try:
        import convertapi
        from dotenv import load_dotenv
        from global_function import get_execution_start_time, get_execution_end_time

    except ModuleNotFoundError:
        os.system('python -m pip install --upgrade pip')
        os.system('pip install --no-cache-dir --upgrade convertapi')
        os.system('pip install --no-cache-dir --upgrade python-dotenv')

    load_dotenv()
    start = get_execution_start_time()

    convertapi.api_secret = os.environ.get('CONVERT_API_SECRET', None)


    # ! Avg upload speed is 2.5 mbps. No cap for download speed.

    print('Uploading & then converting ...')



    # ? Convert docx to pdf.
    # * Took 12 secs for 1.25 MB docx file
    # result = convertapi.convert('pdf', {
    #     'File': f'{os.getcwd()}\\test_files\\demo.docx'
    #     , 'FileName': 'CustomFileName'
    # }, from_format = 'docx')


    # ? Convert jpeg to pdf.
    # * Took 1 min 5 secs for 15.1 MB jpeg file
    # result = convertapi.convert('pdf', {
    #     'File': f'{os.getcwd()}\\test_files\\Large Sample-Image-download-for-Testing.jpeg'
    #     , 'FileName': 'CustomFileName'
    # }, from_format = 'jpeg')


    # ? Convert jpg to pdf.
    # * Took 1 min 5 secs for 15.1 MB jpg file
    # result = convertapi.convert('pdf', {
    #     'File': f'{os.getcwd()}\\test_files\\Large-Sample-Image-download-for Testing.jpg'
    #     , 'FileName': 'CustomFileName'
    # }, from_format = 'jpg')


    # ? Convert pptx to pdf.
    # * Took 1 min 13 secs for 9.75 MB pptx file
    # result = convertapi.convert('pdf', {
    #     'File': f'{os.getcwd()}\\test_files\\PPT-56-Months.Eng 1st-Feb_2019RevisedLR.pptx'
    #     , 'FileName': 'CustomFileName'
    # }, from_format = 'pptx')


    # ? Convert dwg to pdf.
    # * Tested on 49 MB dwg file. Took 3 mins to upload file, 4 mins to process and download instantly.
    # * Test - 1 : Total time taken 11 mins 16 secs for 49 MB dwg file
    # * Test - 2 : Total time taken 7 mins 15 secs for same 49 MB dwg file
    # result = convertapi.convert('pdf', {
    #     'File': f'{os.getcwd()}\\test_files\\prague contour lines.dwg'
    #     , 'FileName': 'CustomFileName'
    # }, from_format = 'dwg')


    # ? Convert bmp to pdf.
    # * Took 3 mins 30 secs for 51.2 MB bmp file
    # result = convertapi.convert('pdf', {
    #     'File': f'{os.getcwd()}\\test_files\\sample 5184×3456.bmp'
    #     , 'FileName': 'CustomFileName'
    # }, from_format = 'bmp')


    # ? Converting doc to pdf.
    # * Took 2 mins 50 secs for 4.88 MB doc file
    # result = convertapi.convert('pdf', {
    #     'File': f'{os.getcwd()}\\test_files\\SampleDOCFile 5000kb.doc'
    #     , 'FileName': 'CustomFileName'
    # }, from_format = 'doc')


    # ? Converting png to pdf.
    # * Took 2 mins 11 secs for 31.3 MB png file
    # result = convertapi.convert('pdf', {
    #     'File': f'{os.getcwd()}\\test_files\\SamplePNGImage 30mb.png'
    #     , 'FileName': 'CustomFileName'
    # }, from_format = 'png')


    # ? Convert ppt to pdf.
    # * Took 12 secs for 0.98 MB ppt file
    # result = convertapi.convert('pdf', {
    #     # 'File': f'{os.getcwd()}\\test_files\\SamplePPTFile 1000kb.ppt'
    #     'File': f'{os.getcwd()}\\test_files\\SamplePPTFile 1000kb.ppt'
    #     , 'FileName': 'CustomFileName'
    # }, from_format = 'ppt')


    # ? Convert txt to pdf.
    # * Took 35 secs for 999 KB txt file
    # result = convertapi.convert('pdf', {
    #     'File': f'{os.getcwd()}\\test_files\\SampleTextFile 1000kb.txt'
    #     , 'FileName': 'CustomFileName'
    # }, from_format = 'txt')



    # ? Merge pdf files to one pdf.
    # * Took 4 mins 51 secs to merge 12 files of total size 212 MB. Processing was instant. Time taken only in uploading and downloading.

    # ?  result = convertapi.convert('merge', {
    # ?      'Files[0]': '/path/to/dpa.pdf'
    # ?      , 'Files[1]': '/path/to/sample.pdf'
    # ?      , 'FileName': 'CustomFileName'
    # ?  }, from_format = 'pdf')

    # result = convertapi.convert('merge', {
    #     'Files': [
    #         f'{os.getcwd()}\\test_files\\[READ] Malvino_Electronic-Principles.pdf'
    #         , f'{os.getcwd()}\\output\\demo.pdf'
    #         , f'{os.getcwd()}\\output\\Large Sample-Image-download-for-Testing.pdf'
    #         , f'{os.getcwd()}\\output\\Large-Sample-Image-download-for Testing.pdf'
    #         , f'{os.getcwd()}\\output\\PPT-56-Months.Eng 1st-Feb_2019RevisedLR.pdf'
    #         , f'{os.getcwd()}\\output\\prague contour lines.pdf'
    #         , f'{os.getcwd()}\\output\\sample 5184×3456.pdf'
    #         , f'{os.getcwd()}\\output\\SampleDOCFile 5000kb.pdf'
    #         , f'{os.getcwd()}\\output\\SamplePNGImage 30mb.pdf'
    #         , f'{os.getcwd()}\\output\\SamplePPTFile 1000kb.pdf'
    #         , f'{os.getcwd()}\\output\\SampleTextFile 1000kb.pdf'
    #     ],
    #    'FileName': 'CustomMergedFileName'
    # }, from_format = 'pdf')



    print("Downloading ...")

    result.save_files(f'{os.getcwd()}\\output')

    user_info = convertapi.user()
    print('user_info ---> ', user_info)
    print('user_info SecondsLeft ---> ', user_info['SecondsLeft'])

    conversion_cost = result.conversion_cost
    print("conversion_cost---> ", conversion_cost)


    print('Total time taken::::: ', get_execution_end_time(start))