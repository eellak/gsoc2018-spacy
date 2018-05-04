
##Ελληνικό Ανοιχτό Πανεπιστήμιο - Πρόγραμμα Σπουδών Πληροφορικής
##Πτυχιακή Εργασία: HOU-CS-UGP-2013-18
##"Αλγόριθμοι Αποδοτικής Επιλογής Χαρακτηριστικών για Κατηγοριοποίηση Κειμένου στην Ελληνική Γλώσσα"
##Αλέξανδρος Καλαπόδης
##Επιβλέπων Καθηγητής: Σπύρος Λυκοθανάσης, Τμήμα Μηχανικών Η/Υ & Πληροφορικής, Πανεπιστήμιο Πάτρας

##Implementation in Python of the greek stemmer presented by Giorgios Ntais during his master thesis with title
##"Development of a Stemmer for the Greek Language" in the Department of Computer and Systems Sciences
##at Stockholm's University / Royal Institute of Technology.

##The system takes as input a word and removes its inflexional suffix according to a rule based algorithm.
##The algorithm follows the known Porter algorithm for the English language and it is developed according to the
##grammatical rules of the Modern Greek language.

VOWELS = ['Α', 'Ε', 'Η', 'Ι', 'Ο', 'Υ', 'Ω', 'Ά', 'Έ', 'Ή', 'Ί', 'Ό', 'Ύ', 'Ώ', 'Ϊ', 'Ϋ']

def ends_with(word, suffix):
    return word[len(word) - len(suffix):] == suffix

def stem(word):

    done = len(word) <= 3
    
    ##rule-set  1
    ##ΓΙΑΓΙΑΔΕΣ->ΓΙΑΓ, ΟΜΑΔΕΣ->ΟΜΑΔ
    if not done:
        for suffix in ['ΙΑΔΕΣ', 'ΑΔΕΣ', 'ΑΔΩΝ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                remaining_part_does_not_end_on = True
                for s in ['ΟΚ', 'ΜΑΜ', 'ΜΑΝ', 'ΜΠΑΜΠ', 'ΠΑΤΕΡ', 'ΓΙΑΓ', 'ΝΤΑΝΤ', 'ΚΥΡ', 'ΘΕΙ', 'ΠΕΘΕΡ']:
                    if ends_with(word, s):
                        remaining_part_does_not_end_on = False
                        break
                if remaining_part_does_not_end_on:
                    word = word + 'ΑΔ'
                done = True
                break

    ##rule-set  2
    ##ΚΑΦΕΔΕΣ->ΚΑΦ, ΓΗΠΕΔΩΝ->ΓΗΠΕΔ
    if not done:
        for suffix in ['ΕΔΕΣ', 'ΕΔΩΝ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in ['ΟΠ', 'ΙΠ', 'ΕΜΠ', 'ΥΠ', 'ΓΗΠ', 'ΔΑΠ', 'ΚΡΑΣΠ', 'ΜΙΛ']:
                    if ends_with(word, s):
                        word = word + 'ΕΔ'
                        break
                done = True
                break

    ##rule-set  3
    ##ΠΑΠΠΟΥΔΩΝ->ΠΑΠΠ, ΑΡΚΟΥΔΕΣ->ΑΡΚΟΥΔ
    if not done:
        for suffix in ['ΟΥΔΕΣ', 'ΟΥΔΩΝ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in ['ΑΡΚ', 'ΚΑΛΙΑΚ', 'ΠΕΤΑΛ', 'ΛΙΧ', 'ΠΛΕΞ', 'ΣΚ', 'Σ', 'ΦΛ', 'ΦΡ', 'ΒΕΛ', 'ΛΟΥΛ', 'ΧΝ', 'ΣΠ', 'ΤΡΑΓ', 'ΦΕ']:
                    if ends_with(word, s):
                        word = word + 'ΟΥΔ'
                        break
                done = True
                break

    ##rule-set  4
    ##ΥΠΟΘΕΣΕΩΣ->ΥΠΟΘΕΣ, ΘΕΩΝ->ΘΕ
    if not done:
        for suffix in ['ΕΩΣ', 'ΕΩΝ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in ['Θ', 'Δ', 'ΕΛ', 'ΓΑΛ', 'Ν', 'Π', 'ΙΔ', 'ΠΑΡ']:
                    if ends_with(word, s):
                        word = word + 'Ε'
                        break
                done = True
                break

    ##rule-set  5
    ##ΠΑΙΔΙΑ->ΠΑΙΔ, ΤΕΛΕΙΟΥ->ΤΕΛΕΙ
    if not done:
        for suffix in ['ΙΑ', 'ΙΟΥ', 'ΙΩΝ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in VOWELS:
                    if ends_with(word, s):
                        word = word + 'Ι'
                        break
                done = True
                break

    ##rule-set  6
    ##ΖΗΛΙΑΡΙΚΟ->ΖΗΛΙΑΡ, ΑΓΡΟΙΚΟΣ->ΑΓΡΟΙΚ
    if not done:
        for suffix in ['ΙΚΑ', 'ΙΚΟΥ', 'ΙΚΩΝ', 'ΙΚΟΣ', 'ΙΚΟ', 'ΙΚΗ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΑΛ', 'ΑΔ', 'ΕΝΔ', 'ΑΜΑΝ', 'ΑΜΜΟΧΑΛ', 'ΗΘ', 'ΑΝΗΘ', 'ΑΝΤΙΔ', 'ΦΥΣ', 'ΒΡΩΜ', 'ΓΕΡ', 'ΕΞΩΔ', 'ΚΑΛΠ',
                            'ΚΑΛΛΙΝ', 'ΚΑΤΑΔ', 'ΜΟΥΛ', 'ΜΠΑΝ', 'ΜΠΑΓΙΑΤ', 'ΜΠΟΛ', 'ΜΠΟΣ', 'ΝΙΤ', 'ΞΙΚ', 'ΣΥΝΟΜΗΛ', 'ΠΕΤΣ', 'ΠΙΤΣ',
                            'ΠΙΚΑΝΤ', 'ΠΛΙΑΤΣ', 'ΠΟΝΤ', 'ΠΟΣΤΕΛΝ', 'ΠΡΩΤΟΔ', 'ΣΕΡΤ', 'ΣΥΝΑΔ', 'ΤΣΑΜ', 'ΥΠΟΔ', 'ΦΙΛΟΝ', 'ΦΥΛΟΔ',
                            'ΧΑΣ']:
                    word = word + 'ΙΚ'
                else:
                    for s in VOWELS:
                        if ends_with(word, s):
                            word = word + 'ΙΚ'
                            break
                done = True
                break

    ##rule-set  7
    ##ΑΓΑΠΑΓΑΜΕ->ΑΓΑΠ, ΑΝΑΠΑΜΕ->ΑΝΑΠΑΜ
    if not done:
        if word == 'ΑΓΑΜΕ': word = 2*word
        for suffix in ['ΗΘΗΚΑΜΕ', 'ΑΓΑΜΕ', 'ΗΣΑΜΕ', 'ΟΥΣΑΜΕ', 'ΗΚΑΜΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['Φ']:
                    word = word + 'ΑΓΑΜ'
                done = True
                break
        if not done and ends_with(word, 'ΑΜΕ'):
            word = word[:len(word) - len('ΑΜΕ')]
            if word in ['ΑΝΑΠ', 'ΑΠΟΘ', 'ΑΠΟΚ', 'ΑΠΟΣΤ', 'ΒΟΥΒ', 'ΞΕΘ', 'ΟΥΛ', 'ΠΕΘ', 'ΠΙΚΡ', 'ΠΟΤ', 'ΣΙΧ', 'Χ']:
                word = word + 'ΑΜ'
            done = True

    ##rule-set  8
    ##ΑΓΑΠΗΣΑΜΕ->ΑΓΑΠ, ΤΡΑΓΑΝΕ->ΤΡΑΓΑΝ
    if not done:
        for suffix in ['ΙΟΥΝΤΑΝΕ', 'ΙΟΝΤΑΝΕ', 'ΟΥΝΤΑΝΕ', 'ΗΘΗΚΑΝΕ', 'ΟΥΣΑΝΕ', 'ΙΟΤΑΝΕ', 'ΟΝΤΑΝΕ', 'ΑΓΑΝΕ', 'ΗΣΑΝΕ',
                       'ΟΤΑΝΕ', 'ΗΚΑΝΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΤΡ', 'ΤΣ', 'Φ']:
                    word = word + 'ΑΓΑΝ'
                done = True
                break
        if not done and ends_with(word, 'ΑΝΕ'):
            word = word[:len(word) - len('ΑΜΕ')]
            if word in ['ΒΕΤΕΡ', 'ΒΟΥΛΚ', 'ΒΡΑΧΜ', 'Γ', 'ΔΡΑΔΟΥΜ', 'Θ', 'ΚΑΛΠΟΥΖ', 'ΚΑΣΤΕΛ', 'ΚΟΡΜΟΡ', 'ΛΑΟΠΛ', 'ΜΩΑΜΕΘ', 'Μ',
                        'ΜΟΥΣΟΥΛΜ', 'Ν', 'ΟΥΛ', 'Π', 'ΠΕΛΕΚ', 'ΠΛ', 'ΠΟΛΙΣ', 'ΠΟΡΤΟΛ', 'ΣΑΡΑΚΑΤΣ', 'ΣΟΥΛΤ', 'ΤΣΑΡΛΑΤ', 'ΟΡΦ',
                        'ΤΣΙΓΓ', 'ΤΣΟΠ', 'ΦΩΤΟΣΤΕΦ', 'Χ', 'ΨΥΧΟΠΛ', 'ΑΓ', 'ΟΡΦ', 'ΓΑΛ', 'ΓΕΡ', 'ΔΕΚ', 'ΔΙΠΛ', 'ΑΜΕΡΙΚΑΝ', 'ΟΥΡ',
                        'ΠΙΘ', 'ΠΟΥΡΙΤ', 'Σ', 'ΖΩΝΤ', 'ΙΚ', 'ΚΑΣΤ', 'ΚΟΠ', 'ΛΙΧ', 'ΛΟΥΘΗΡ', 'ΜΑΙΝΤ', 'ΜΕΛ', 'ΣΙΓ', 'ΣΠ', 'ΣΤΕΓ',
                        'ΤΡΑΓ', 'ΤΣΑΓ', 'Φ', 'ΕΡ', 'ΑΔΑΠ', 'ΑΘΙΓΓ', 'ΑΜΗΧ', 'ΑΝΙΚ', 'ΑΝΟΡΓ', 'ΑΠΗΓ', 'ΑΠΙΘ', 'ΑΤΣΙΓΓ', 'ΒΑΣ',
                        'ΒΑΣΚ', 'ΒΑΘΥΓΑΛ', 'ΒΙΟΜΗΧ', 'ΒΡΑΧΥΚ', 'ΔΙΑΤ', 'ΔΙΑΦ', 'ΕΝΟΡΓ', 'ΘΥΣ', 'ΚΑΠΝΟΒΙΟΜΗΧ', 'ΚΑΤΑΓΑΛ', 'ΚΛΙΒ',
                        'ΚΟΙΛΑΡΦ', 'ΛΙΒ', 'ΜΕΓΛΟΒΙΟΜΗΧ', 'ΜΙΚΡΟΒΙΟΜΗΧ', 'ΝΤΑΒ', 'ΞΗΡΟΚΛΙΒ', 'ΟΛΙΓΟΔΑΜ', 'ΟΛΟΓΑΛ', 'ΠΕΝΤΑΡΦ',
                        'ΠΕΡΗΦ', 'ΠΕΡΙΤΡ', 'ΠΛΑΤ', 'ΠΟΛΥΔΑΠ', 'ΠΟΛΥΜΗΧ', 'ΣΤΕΦ', 'ΤΑΒ', 'ΤΕΤ', 'ΥΠΕΡΗΦ', 'ΥΠΟΚΟΠ', 'ΧΑΜΗΛΟΔΑΠ',
                        'ΨΗΛΟΤΑΒ']:
                word = word + 'ΑΝ'
            else:
                for s in VOWELS:
                    if ends_with(word, s):
                        word = word + 'ΑΝ'
                        break
            done = True

    ##rule-set  9
    ##ΑΓΑΠΗΣΕΤΕ->ΑΓΑΠ, ΒΕΝΕΤΕ->ΒΕΝΕΤ
    if not done:
        if ends_with(word, 'ΗΣΕΤΕ'):
            word = word[:len(word) - len('ΗΣΕΤΕ')]
            done = True
        elif ends_with(word, 'ΕΤΕ'):
            word = word[:len(word) - len('ΕΤΕ')]
            if word in ['ΑΒΑΡ', 'ΒΕΝ', 'ΕΝΑΡ', 'ΑΒΡ', 'ΑΔ', 'ΑΘ', 'ΑΝ', 'ΑΠΛ', 'ΒΑΡΟΝ', 'ΝΤΡ', 'ΣΚ', 'ΚΟΠ', 'ΜΠΟΡ', 'ΝΙΦ', 'ΠΑΓ',
                        'ΠΑΡΑΚΑΛ', 'ΣΕΡΠ', 'ΣΚΕΛ', 'ΣΥΡΦ', 'ΤΟΚ', 'Υ', 'Δ', 'ΕΜ', 'ΘΑΡΡ', 'Θ']:
                word = word + 'ΕΤ'
            else:
                for s in ['ΟΔ', 'ΑΙΡ', 'ΦΟΡ', 'ΤΑΘ', 'ΔΙΑΘ', 'ΣΧ', 'ΕΝΔ', 'ΕΥΡ', 'ΤΙΘ', 'ΥΠΕΡΘ', 'ΡΑΘ', 'ΕΝΘ', 'ΡΟΘ', 'ΣΘ', 'ΠΥΡ',
                          'ΑΙΝ', 'ΣΥΝΔ', 'ΣΥΝ', 'ΣΥΝΘ', 'ΧΩΡ', 'ΠΟΝ', 'ΒΡ', 'ΚΑΘ', 'ΕΥΘ', 'ΕΚΘ', 'ΝΕΤ', 'ΡΟΝ', 'ΑΡΚ', 'ΒΑΡ', 'ΒΟΛ',
                          'ΩΦΕΛ'] + VOWELS:
                    if ends_with(word, s):
                        word = word + 'ΕΤ'
                        break
            done = True

    ##rule-set 10
    ##ΑΓΑΠΩΝΤΑΣ->ΑΓΑΠ, ΞΕΝΟΦΩΝΤΑΣ->ΞΕΝΟΦΩΝ
    if not done:
        for suffix in ['ΟΝΤΑΣ', 'ΩΝΤΑΣ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΑΡΧ']:
                    word = word + 'ΟΝΤ'
                elif word in ['ΞΕΝΟΦ', 'ΚΡΕ']:
                    word = word + 'ΩΝΤ'
                done = True
                break

    ##rule-set 11
    ##ΑΓΑΠΙΟΜΑΣΤΕ->ΑΓΑΠ, ΟΝΟΜΑΣΤΕ->ΟΝΟΜΑΣΤ
    if not done:
        for suffix in ['ΙΟΜΑΣΤΕ', 'ΟΜΑΣΤΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΟΝ']:
                    word = word + 'ΟΜΑΣΤ'
                done = True
                break

    ##rule-set 12
    ##ΑΓΑΠΙΕΣΤΕ->ΑΓΑΠ, ΠΙΕΣΤΕ->ΠΙΕΣΤ
    if not done:
        for suffix in ['ΙΕΣΤΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['Π', 'ΑΠ', 'ΣΥΜΠ', 'ΑΣΥΜΠ', 'ΚΑΤΑΠ', 'ΜΕΤΑΜΦ']:
                    word = word + 'ΙΕΣΤ'
                done = True
                break
    if not done:
        for suffix in ['ΕΣΤΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΑΛ', 'ΑΡ', 'ΕΚΤΕΛ', 'Ζ', 'Μ', 'Ξ', 'ΠΑΡΑΚΑΛ', 'ΑΡ', 'ΠΡΟ', 'ΝΙΣ']:
                    word = word + 'ΕΣΤ'
                done = True
                break

    ##rule-set 13
    ##ΧΤΙΣΤΗΚΕ->ΧΤΙΣΤ, ΔΙΑΘΗΚΕΣ->ΔΙΑΘΗΚ
    if not done:
        for suffix in ['ΗΘΗΚΑ', 'ΗΘΗΚΕΣ', 'ΗΘΗΚΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                done = True
                break
    if not done:
        for suffix in ['ΗΚΑ', 'ΗΚΕΣ', 'ΗΚΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΔΙΑΘ', 'Θ', 'ΠΑΡΑΚΑΤΑΘ', 'ΠΡΟΣΘ', 'ΣΥΝΘ']:
                    word = word + 'ΗΚ'
                else:
                    for suffix in ['ΣΚΩΛ', 'ΣΚΟΥΛ', 'ΝΑΡΘ', 'ΣΦ', 'ΟΘ', 'ΠΙΘ']:
                        if ends_with(word, suffix):
                            word = word + 'ΗΚ'
                            break
                done = True
                break
            
    ##rule-set 14
    ##ΧΤΥΠΟΥΣΕΣ->ΧΤΥΠ, ΜΕΔΟΥΣΕΣ->ΜΕΔΟΥΣ
    if not done:
        for suffix in ['ΟΥΣΑ', 'ΟΥΣΕΣ', 'ΟΥΣΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΦΑΡΜΑΚ', 'ΧΑΔ', 'ΑΓΚ', 'ΑΝΑΡΡ', 'ΒΡΟΜ', 'ΕΚΛΙΠ', 'ΛΑΜΠΙΔ', 'ΛΕΧ', 'Μ', 'ΠΑΤ', 'Ρ', 'Λ', 'ΜΕΔ', 'ΜΕΣΑΖ',
                            'ΥΠΟΤΕΙΝ', 'ΑΜ', 'ΑΙΘ', 'ΑΝΗΚ', 'ΔΕΣΠΟΖ', 'ΕΝΔΙΑΦΕΡ', 'ΔΕ', 'ΔΕΥΤΕΡΕΥ', 'ΚΑΘΑΡΕΥ', 'ΠΛΕ', 'ΤΣΑ']:
                    word = word + 'ΟΥΣ'
                else:
                    for s in ['ΠΟΔΑΡ', 'ΒΛΕΠ', 'ΠΑΝΤΑΧ', 'ΦΡΥΔ', 'ΜΑΝΤΙΛ', 'ΜΑΛΛ', 'ΚΥΜΑΤ', 'ΛΑΧ', 'ΛΗΓ', 'ΦΑΓ', 'ΟΜ', 'ΠΡΩΤ'] + VOWELS:
                        if ends_with(word, s):
                            word = word + 'ΟΥΣ'
                            break
                done = True
                break

    ##rule-set 15
    #ΚΟΛΛΑΓΕΣ->ΚΟΛΛ, ΑΒΑΣΤΑΓΑ->ΑΒΑΣΤ
    if not done:
        for suffix in ['ΑΓΑ', 'ΑΓΕΣ', 'ΑΓΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΑΒΑΣΤ', 'ΠΟΛΥΦ', 'ΑΔΗΦ', 'ΠΑΜΦ', 'Ρ', 'ΑΣΠ', 'ΑΦ', 'ΑΜΑΛ', 'ΑΜΑΛΛΙ', 'ΑΝΥΣΤ', 'ΑΠΕΡ', 'ΑΣΠΑΡ', 'ΑΧΑΡ',
                            'ΔΕΡΒΕΝ', 'ΔΡΟΣΟΠ', 'ΞΕΦ', 'ΝΕΟΠ', 'ΝΟΜΟΤ', 'ΟΛΟΠ', 'ΟΜΟΤ', 'ΠΡΟΣΤ', 'ΠΡΟΣΩΠΟΠ', 'ΣΥΜΠ', 'ΣΥΝΤ', 'Τ',
                            'ΥΠΟΤ', 'ΧΑΡ', 'ΑΕΙΠ', 'ΑΙΜΟΣΤ', 'ΑΝΥΠ', 'ΑΠΟΤ', 'ΑΡΤΙΠ', 'ΔΙΑΤ', 'ΕΝ', 'ΕΠΙΤ', 'ΚΡΟΚΑΛΟΠ', 'ΣΙΔΗΡΟΠ',
                            'Λ', 'ΝΑΥ', 'ΟΥΛΑΜ', 'ΟΥΡ', 'Π', 'ΤΡ', 'Μ']:
                    word = word + 'ΑΓ'
                else:
                    for s in ['ΟΦ', 'ΠΕΛ', 'ΧΟΡΤ', 'ΣΦ', 'ΡΠ', 'ΦΡ', 'ΠΡ', 'ΛΟΧ', 'ΣΜΗΝ']:
                        # ΑΦΑΙΡΕΘΗΚΕ: 'ΛΛ'
                        if ends_with(word, s):
                            if not word in ['ΨΟΦ', 'ΝΑΥΛΟΧ']:
                                word = word + 'ΑΓ'
                            break
                done = True
                break

    ##rule-set 16
    ##ΑΓΑΠΗΣΕ->ΑΓΑΠ, ΝΗΣΟΥ->ΝΗΣ
    if not done:
        for suffix in ['ΗΣΕ', 'ΗΣΟΥ', 'ΗΣΑ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['Ν', 'ΧΕΡΣΟΝ', 'ΔΩΔΕΚΑΝ', 'ΕΡΗΜΟΝ', 'ΜΕΓΑΛΟΝ', 'ΕΠΤΑΝ', 'ΑΓΑΘΟΝ']:
                    word = word + 'ΗΣ'
                done = True
                break
            
    ##rule-set 17
    ##ΑΓΑΠΗΣΤΕ->ΑΓΑΠ, ΣΒΗΣΤΕ->ΣΒΗΣΤ
    if not done:
        for suffix in ['ΗΣΤΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΑΣΒ', 'ΣΒ', 'ΑΧΡ', 'ΧΡ', 'ΑΠΛ', 'ΑΕΙΜΝ', 'ΔΥΣΧΡ', 'ΕΥΧΡ', 'ΚΟΙΝΟΧΡ', 'ΠΑΛΙΜΨ']:
                    word = word + 'ΗΣΤ'
                done = True
                break
            
    ##rule-set 18
    ##ΑΓΑΠΟΥΝΕ->ΑΓΑΠ, ΣΠΙΟΥΝΕ->ΣΠΙΟΥΝ
    if not done:
        for suffix in ['ΟΥΝΕ', 'ΗΣΟΥΝΕ', 'ΗΘΟΥΝΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['Ν', 'Ρ', 'ΣΠΙ', 'ΣΤΡΑΒΟΜΟΥΤΣ', 'ΚΑΚΟΜΟΥΤΣ', 'ΕΞΩΝ']:
                    word = word + 'OYN'
                done = True
                break
            
    ##rule-set 19
    ##ΑΓΑΠΟΥΜΕ->ΑΓΑΠ, ΦΟΥΜΕ->ΦΟΥΜ
    if not done:
        for suffix in ['ΟΥΜΕ', 'ΗΣΟΥΜΕ', 'ΗΘΟΥΜΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΠΑΡΑΣΟΥΣ', 'Φ', 'Χ', 'ΩΡΙΟΠΛ', 'ΑΖ', 'ΑΛΛΟΣΟΥΣ', 'ΑΣΟΥΣ']:
                    word = word + 'ΟΥΜ'
                done = True
                break
            
    ##rule-set 20
    ##ΚΥΜΑΤΑ->ΚΥΜ, ΧΩΡΑΤΟ->ΧΩΡΑΤ
    if not done:
        for suffix in ['ΜΑΤΑ', 'ΜΑΤΩΝ', 'ΜΑΤΟΣ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                word = word + 'Μ'
                done = True
                break
            
    ##rule-set 21
    if not done:
        for suffix in ['ΙΟΝΤΟΥΣΑΝ', 'ΙΟΥΜΑΣΤΕ', 'ΙΟΜΑΣΤΑΝ', 'ΙΟΣΑΣΤΑΝ', 'ΟΝΤΟΥΣΑΝ', 'ΙΟΣΑΣΤΕ', 'ΙΕΜΑΣΤΕ', 'ΙΕΣΑΣΤΕ', 'ΙΟΜΟΥΝΑ',
                       'ΙΟΣΟΥΝΑ', 'ΙΟΥΝΤΑΙ', 'ΙΟΥΝΤΑΝ', 'ΗΘΗΚΑΤΕ', 'ΟΜΑΣΤΑΝ', 'ΟΣΑΣΤΑΝ', 'ΟΥΜΑΣΤΕ', 'ΙΟΜΟΥΝ', 'ΙΟΝΤΑΝ', 'ΙΟΣΟΥΝ',
                       'ΗΘΕΙΤΕ', 'ΗΘΗΚΑΝ', 'ΟΜΟΥΝΑ', 'ΟΣΑΣΤΕ', 'ΟΣΟΥΝΑ', 'ΟΥΝΤΑΙ', 'ΟΥΝΤΑΝ', 'ΟΥΣΑΤΕ',  'ΑΓΑΤΕ', 'ΕΙΤΑΙ', 'ΙΕΜΑΙ',
                       'ΙΕΤΑΙ', 'ΙΕΣΑΙ', 'ΙΟΤΑΝ', 'ΙΟΥΜΑ', 'ΗΘΕΙΣ', 'ΗΘΟΥΝ', 'ΗΚΑΤΕ', 'ΗΣΑΤΕ', 'ΗΣΟΥΝ', 'ΟΜΟΥΝ',  'ΟΝΤΑΙ',
                       'ΟΝΤΑΝ', 'ΟΣΟΥΝ', 'ΟΥΜΑΙ', 'ΟΥΣΑΝ',  'ΑΓΑΝ', 'ΑΜΑΙ', 'ΑΣΑΙ', 'ΑΤΑΙ', 'ΕΙΤΕ', 'ΕΣΑΙ', 'ΕΤΑΙ', 'ΗΔΕΣ',
                       'ΗΔΩΝ', 'ΗΘΕΙ', 'ΗΚΑΝ', 'ΗΣΑΝ', 'ΗΣΕΙ', 'ΗΣΕΣ', 'ΟΜΑΙ', 'ΟΤΑΝ',  'ΑΕΙ',  'ΕΙΣ',  'ΗΘΩ',  'ΗΣΩ', 'ΟΥΝ',
                       'ΟΥΣ',  'ΑΝ', 'ΑΣ', 'ΑΩ', 'ΕΙ', 'ΕΣ', 'ΗΣ', 'ΟΙ', 'ΟΝ', 'ΟΣ', 'ΟΥ', 'ΥΣ', 'ΩΝ', 'ΩΣ', 'Α', 'Ε', 'Ι', 'Η',
                       'Ο',  'Υ', 'Ω']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                break

    ##rule-set 22
    ##ΠΛΗΣΙΕΣΤΑΤΟΣ->ΠΛΥΣΙ, ΜΕΓΑΛΥΤΕΡΗ->ΜΕΓΑΛ, ΚΟΝΤΟΤΕΡΟ->ΚΟΝΤ
    if not done:
        for suffix in ['ΕΣΤΕΡ', 'ΕΣΤΑΤ', 'ΟΤΕΡ', 'ΟΤΑΤ', 'ΥΤΕΡ', 'ΥΤΑΤ', 'ΩΤΕΡ', 'ΩΤΑΤ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                break
            
    return word
