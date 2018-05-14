# removes files
python3 personal_parser.py > norms_from_dict.out
# finders
python3 finder_adj_norms_1.py > adj_norms_1.txt
python3 finder_adj_norms_2.py > adj_norms_2.txt
python3 finder_adj_norms_3.py > adj_norms_3.txt
python3 finder_adj_norms_4.py > adj_norms_4.txt
# parsers
python3 parser_adj_norms_1.py > adj_norms_1_parsed.out
python3 parser_adj_norms_2.py > adj_norms_2_parsed.out
python3 parser_adj_norms_3.py > adj_norms_3_parsed.out
python3 parser_adj_norms_4.py > adj_norms_4_parsed.out

# alltogether
python3 merger.py > all.out
python3 checker.py > final.out