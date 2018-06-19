# About this file

Hello reader! We hope that this file will help you understand how spaCy works and the way in which our model for Greek language is structured.


## Understanding different Greek language models

spaCy comes with more than one model for each language. 
For Greek model we define the following models:

1. el_lang_sm: Contains the basics (lemmatizer, lexical attributes, punctuation rules, syntax iterators, tag map, norm exceptions and tokenizer exceptions).
2. el_lang_md: Contains the basics + named entities trained model + trained pos tagger.
3. el_lang_lg: Contains basics + named entities trained model + trained pos tagger + Word Vectors.




## Understanding POS tagger

Greek pos tagger is based on Universal POS tags model. 
There are the following possible tags for a word:

1. adj: επίθετα
2. adv: επιρρήματα
3. adp: προθέσεις
4. aux: ρήματα για σχηματισμό χρόνων
5. intj: επιφωνήματα
6. propn: ουσιαστικά που χρησιμοποιούνται ως ονόματα
7. verb: ρήματα
8. cconj: παρατακτικοί σύνδεσμοι
9. sconj: υποτακτικοί σύνδεσμοι
10. part: μόρια
11. punct: σημεία στίξης
12. sym: σύμβολα
13. num: αριθμητικά
14. pron: αντωνυμίες
15. space: κενό
16. det: άρθρα
17. noun: ουσιαστικά


## Understanding NER

Ner supports the following tags:

1. PERSON: άνθρωποι (συμπεριλαμβάνονται φανταστικοί χαρακτήρες όπως Mr Bean)
2. NORP: Εθνικότητες, θρησκείες ή πολιτικές οργανώσεις
3. FAC: κτίρια
4. ORG: οργανισμοί/επιχείρησεις
5. GPE: Χώρες, πόλεις, χωριά, πολιτείες
6. LOC: Βουνά, Θάλασσες, ποτάμια, λίμνες
7. PRODUCT: προϊόντα
8. EVENT: ιστορικά και άλλα γεγονότα
9. WORK_OF_ART: έργα τέχνης
10. LAW: νόμοι
11. LANGUAGE: γλώσσες
12. DATE: ημερομηνίες ή χρονικές περίοδοι (πχ. Μεσσαίωνας)
13. TIME: χρόνος μικρότερος της μέρας
14. PERCENT: ποσοστό
15. MONEY: χρηματικές μονάδες (πχ ευρώ)
16. QUANTITY: μετρήσεις ποσοτήτων
17. ORDINAL: πρώτος, δεύτερος, κλπ
18. CARDINAL: αριθμητικά που δεν ανήκουν σε κάποια από τις παραπάνω κατηγορίες



## Understanding Dependencies

1. ACL: Clausal modifier of noun
2. ACOMP: Adjectival complement
3. ADVCL: Adverbial clause modifier
4. ADVMOD: επιρρηματικός προσδιορισμός	
5. AGENT: Agent
6. AMOD: Adjectival modifier
7. APPOS: Appositional modifier
8. ATTR: Attribute
9. AUX: Auxiliary
10. AUXPASS: Auxiliary (passive)
11. CASE: Case marker
12. CC: Coordinating conjunction
13. CCOMP: Clausal complement
14. COMPOUND: Compound modifier
15. CONJ: Conjunct
16. CSUBJ: Clausal subject
17. CSUBJPASS: Clausal subject (passive)
18. DATIVE: Dative
19. DEP: Unclassified dependent
20. DET: Determiner
21. DOBJ: Direct Object
22. EXPL: Expletive
23. INTJ: Interjection
24. MARK: Marker
25. META: Meta modifier
26. NEG: Negation modifier
27. NOUNMOD: Modifier of nominal
28. NPMOD: Noun phrase as adverbial modifier
29. NSUBJ: Nominal subject
30. NSUBJPASS: Nominal subject (passive)
31. NUMMOD: Number modifier
32. OPRD: Object predicate
33. PARATAXIS: Parataxis
34. PCOMP: Complement of preposition
35. POBJ: Object of preposition
36. POSS: Possession modifier
37. PRECONJ: Pre-correlative conjunction
38. PREDET: Pre-determiner
39. PREP: Prepositional modifier
40. PRT: Particle
41. PUNCT: Punctuation
42. QUANTMOD: Modifier of quantifier
43. RELCL: Relative clause modifier
44. ROOT: Root
45. XCOMP: Open clausal complement


## Understanding project structure

### Stop-words


1. global-freqs/ : Contains code and out files needed for creating nlp vocab.





