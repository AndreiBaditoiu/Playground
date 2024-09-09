import sys
import PyPDF2
"""PYPDF2 used here is deprecated, 
therefore using updated module 
implies updating syntax too.
"""

# with open('dummy.pdf', 'rb') as file:
# 	reader = PyPDF2.PdfFileReader(file)
# 	page = reader.getPage(0)
# 	page.rotateCounterClockwise(90)
# 	writer = PyPDF2.PdfFileWriter()
# 	writer.addPage(page)
# 	with open('tilt.pdf', 'wb') as new_file:
# 		writer.write(new_file)


# PDF Merger

# inputs = sys.argv[1:]
#
#
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')
#
#
# pdf_combiner(inputs)
#

# PDF Watermarker

# watermark = PyPDF2.PdfFileReader('wtr.pdf')
# reader = PyPDF2.PdfFileReader("super.pdf")
# page = reader.pages[0]
# page.mergePage(watermark.pages[0])

# writer = PdfFileWriter()
# writer.addPage(page)

# with open("PyPDF2-output.pdf", "wb") as fp:
#     writer.write(fp)
#     # output.write(fp)


#/////

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open('watermarked_output.pdf', 'wb') as file:
		output.write(file)



