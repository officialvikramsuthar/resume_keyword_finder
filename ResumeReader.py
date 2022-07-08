import yake
import pdfplumber

def KeywordExtractorFun(text):
	kw_extractor = yake.KeywordExtractor()
	#text = """spaCy is an open-source software library for advanced natural language processing, written in the programming languages Python and Cython. The library is published under the MIT license and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion."""
	language = "en"
	max_ngram_size = 3
	deduplication_threshold = 0.9
	numOfKeywords = 30
	custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
	keywords = custom_kw_extractor.extract_keywords(text)
	for kw in keywords:
		print(kw)

def PDFrotate(origFileName, newFileName, rotation):
	text = ""

	with pdfplumber.open("resume.pdf") as pdf:
		for i in range(len(pdf.pages)):
			first_page = pdf.pages[i]
			text = text + first_page.extract_text()

	KeywordExtractorFun(text)
	

def main():

	# original pdf file name
	origFileName = 'resume.pdf'
	
	# new pdf file name
	newFileName = 'rotated_example.pdf'
	
	# rotation angle
	rotation = 270
	
	# calling the PDFrotate function
	PDFrotate(origFileName, newFileName, rotation)
	
# if _name_ == "_main_":
# 	# calling the main function
main()