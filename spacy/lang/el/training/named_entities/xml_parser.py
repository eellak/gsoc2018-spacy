import re
import glob, os
import spacy
import xml.etree.ElementTree as ET
os.chdir("xml_datasets/")
sentences=[]
nlp=spacy.load('el_unnamed')
for file in glob.glob("*.xml"):
	tree = ET.parse('{}'.format(file))
	root = tree.getroot()
	begin=[]
	end=[]
	for child in root:
		if (child.tag=='{http:///uima/cas.ecore}Sofa'):
			txt=child.attrib['sofaString']
		if (child.tag=='{http:///gr/ilsp/types.ecore}Sentence'):
			begin.append(int(child.attrib['begin']))
			end.append(int(child.attrib['end']))

	for i in range(len(begin)):
		tmp_sentence=txt[begin[i]:end[i]]
		doc=nlp(tmp_sentence)
		flag=False
		for j in doc:
			if (j.tag_=='PROPN'):
				flag=True
		if (flag==True):
			sentences.append(tmp_sentence)
	for x in sentences:
		print(x)


	

