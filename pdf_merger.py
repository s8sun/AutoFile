import PyPDF2 
import argparse

def PDFmerge(pdfs, output):  
	pdfMerger = PyPDF2.PdfFileMerger() 
	for pdf in pdfs: 
		pdfMerger.append(PyPDF2.PdfFileReader(pdf),'rb') 
	with open(output, 'wb') as f: 
		pdfMerger.write(f) 

if __name__ == "__main__": 
# calling the main function 
	parser = argparse.ArgumentParser()
	parser.add_argument('-i',"--input",metavar='N',nargs='+')
	parser.add_argument('-o',"--output")
	args = parser.parse_args()
	PDFmerge(args.input, args.output) 