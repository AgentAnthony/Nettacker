#!/usr/bin/env python
# -*- coding: utf-8 -*-


def all_messages():
    return \
        {
            "0": "Ο μηχανισμός Nettacker ξεκίνησε ...\n\n",
            "1": "python nettacker.py [επιλογές]",
            "2": "Εμφάνιση του μενού βοήθειας Nettacker",
            "3": "Διαβάστε τις άδειες και τις συμφωνίες https://github.com/viraintel/OWASP-Nettacker\n",
            "4": "Κινητήρας",
            "5": "Επιλογές εισαγωγής κινητήρα",
            "6": "επιλέξτε μια γλώσσα {0}",
            "7": "σάρωση όλων των διευθύνσεων IP στην περιοχή",
            "8": "βρείτε και σαρώστε υποτομείς",
            "9": "αριθμούς νήματος για συνδέσεις σε έναν κεντρικό υπολογιστή",
            "10": "τους αριθμούς νήματος για τους ξενιστές σάρωσης",
            "11": "αποθηκεύστε όλα τα αρχεία καταγραφής στο αρχείο (results.txt, results.html, results.json)",
            "12": "Στόχος",
            "13": "Επιλογές εισαγωγής στόχων",
            "14": "λίστα στόχων, χωριστά με \",\"",
            "15": "να διαβάσετε τους στόχους από το αρχείο",
            "16": "Επιλογές μεθόδου σάρωσης",
            "17": "επιλέξτε τη μέθοδο σάρωσης {0}",
            "18": "επιλέξτε μέθοδο σάρωσης για να εξαιρέσετε {0}",
            "19": "όνομα χρήστη (ες), χωριστά με \",\"",
            "20": "να διαβάσετε το όνομα χρήστη από το αρχείο",
            "21": "λίστα κωδικών πρόσβασης, ξεχωριστά με \",\"",
            "22": "διαβάζουν τον κωδικό πρόσβασης από το αρχείο",
            "23": "λίστα λιμένων, χωριστά με \",\"",
            "24": "να διαβάσει τους κωδικούς πρόσβασης από το αρχείο",
            "25": "χρόνος για ύπνο μεταξύ κάθε αιτήματος",
            "26": "Δεν είναι δυνατός ο προσδιορισμός του στόχου",
            "27": "Δεν είναι δυνατός ο προσδιορισμός των στόχων που δεν μπορούν να ανοίξουν το αρχείο: {0}",
            "28": "είναι καλύτερα να χρησιμοποιήσετε αριθμό νήματος μικρότερο από 100, BTW συνεχίζουμε ...",
            "29": "ορίστε το χρονικό όριο στα {0} δευτερόλεπτα, είναι πολύ μεγάλο, έτσι δεν είναι; από τον τρόπο που συνεχίζουμε ...",
            "30": "αυτή η ενότητα σάρωσης [{0}] δεν βρέθηκε!",
            "31": "αυτή η ενότητα σάρωσης [{0}] δεν βρέθηκε!",
            "32": "δεν μπορείτε να εξαιρέσετε όλες τις μεθόδους σάρωσης",
            "33": "δεν μπορείτε να εξαιρέσετε όλες τις μεθόδους σάρωσης",
            "34": "η {0} ενότητα που επιλέξατε για να εξαιρέσετε δεν βρέθηκε!",
            "35": "εισάγετε τις μεθόδους εισόδου, για παράδειγμα: \"ftp_brute_users = test, admin & ftp_brute_passwds = read_from_file: /tmp/pass.txt&ftp_brute_port=21\"",
            "36": "δεν μπορεί να διαβάσει το αρχείο {0}",
            "37": "Δεν είναι δυνατός ο προσδιορισμός των ονομάτων χρηστών που δεν μπορούν να ανοίξουν το αρχείο: {0}",
            "38": "",
            "39": "Δεν είναι δυνατός ο προσδιορισμός των κωδικών πρόσβασης, δεν είναι δυνατή η ανοίξη αρχείου: {0}",
            "40": "το αρχείο \"{0}\" δεν είναι εγγράψιμο!",
            "41": "επιλέξτε τη μέθοδο σάρωσης!",
            "42": "κατάργηση αρχείων temp!",
            "43": "διαλογή αποτελεσμάτων!",
            "44": "Έγινε!",
            "45": "να αρχίσετε να επιτεθείτε {0}, {1} από {2}",
            "46": "αυτή η ενότητα \"{0}\" δεν είναι διαθέσιμη",
            "47": "δυστυχώς αυτή η έκδοση του λογισμικού θα μπορούσε απλώς να τρέξει σε linux/osx/windows.",
            "48": "Η έκδοση Python δεν υποστηρίζεται!",
            "49": "παρακάμπτοντας τον διπλό στόχο (ορισμένοι υποτομείς / τομείς μπορούν να έχουν το ίδιο IP και εύρος)",
            "50": "άγνωστος τύπος στόχου [{0}]",
            "51": "έλεγχος εύρους {0} ...",
            "52": "έλεγχος {0} ...",
            "53": "ΠΛΗΘΟΣ",
            "54": "USERNAME",
            "55": "ΚΩΔΙΚΟΣ ΠΡΟΣΒΑΣΗΣ",
            "56": "ΛΙΜΑΝΙ",
            "57": "ΤΥΠΟΣ",
            "58": "ΠΕΡΙΓΡΑΦΗ",
            "59": "(0-5) (προεπιλογή 0)",
            "60": "εμφάνιση της έκδοσης λογισμικού",
            "61": "Έλεγχος για ενημερώσεις",
            "62": "",
            "63": "",
            "64": "Επαναλαμβάνει πότε το χρονικό όριο σύνδεσης (προεπιλογή 3)",
            "65": "Σύνδεση ftp με {0}: {1} λήξη χρόνου, παρακάμπτοντας {2}: {3}",
            "66": "ΕΓΓΡΑΦΕΙΤΑΙ ΣΕ ΕΠΙΤΥΧΙΑ!",
            "67": "ΕΓΓΡΑΦΟΜΕΝΗ ΣΕ ΕΠΙΤΥΧΙΑ, ΑΔΕΙΑ ΑΠΑΓΟΡΕΥΕΤΑΙ ΓΙΑ ΔΕΣΜΕΥΣΗ ΚΑΤΑΛΟΓΟΥ!",
            "68": "Η σύνδεση ftp με {0}: {1} απέτυχε, παραλείποντας ολόκληρο το βήμα [διαδικασία {2} της {3}]! πηγαίνετε στο επόμενο βήμα",
            "69": "ο στόχος εισόδου για τη λειτουργική μονάδα {0} πρέπει να είναι DOMAIN, HTTP ή SINGLE_IPv4, παρακάμπτοντας {1}",
            "70": "χρήστη: {0} περάσει: {1} φιλοξενεί: {2} λιμάνι: {3} βρέθηκε!",
            "71": "(ΧΩΡΙΣ ΑΔΕΙΑ ΓΙΑ ΑΡΧΕΙΑ ΚΑΤΑΛΟΓΟΥ)",
            "72": "προσπαθώντας {0} από {1} στη διαδικασία {2} από {3} {4}: {5}",
            "73": "σύνδεση smtp με {0}: {1} timeout, παρακάμπτοντας {2}: {3}",
            "74": "η σύνδεση smtp με {0}: {1} απέτυχε, παρακάμπτοντας ολόκληρο το βήμα [process {2} of {3}]! πηγαίνετε στο επόμενο βήμα",
            "75": "ο στόχος εισόδου για τη {0} μονάδα πρέπει να είναι HTTP, παρακάμπτοντας {1}",
            "76": "σύνδεση ssh με {0}: {1} χρονικό όριο, παρακάμπτοντας {2}: {3}",
            "77": "Η σύνδεση ssh με {0}: {1} απέτυχε, παραλείποντας ολόκληρο το βήμα [διαδικασία {2} της {3}]! πηγαίνετε στο επόμενο βήμα",
            "78": "Η σύνδεση ssh με% s:% s απέτυχε, παραλείποντας ολόκληρο το βήμα [διαδικασία% s του% s]! πηγαίνετε στο επόμενο βήμα",
            "79": "ΑΝΟΙΚΤΟ ΛΙΜΑΝΙ",
            "80": "υποδοχής: {0} θύρα: {1} βρέθηκε!",
            "81": "ο στόχος {0} υποβλήθηκε!",
            "82": "δεν μπορεί να ανοίξει αρχείο λίστας μεσολάβησης: {0}",
            "83": "δεν μπορεί να βρει αρχείο λίστας proxies: {0}",
            "84": "εκτελείτε την έκδοση OWASP Nettacker {0} {1} {2} {6} με το όνομα κώδικα {3} {4} {5}",
            "85": "αυτή η λειτουργία δεν είναι ακόμα διαθέσιμη! εκτελέστε το \"git clone https://github.com/viraintel/OWASP-Nettacker.git\" ή \"pip install -U OWASP-Nettacker\" για να λάβετε την τελευταία έκδοση.",
            "86": "να δημιουργήσετε ένα γράφημα όλων των δραστηριοτήτων και πληροφοριών, πρέπει να χρησιμοποιήσετε την έξοδο HTML. διαθέσιμα γραφήματα: {0}",
            "87": "για να χρησιμοποιήσετε τη γραφική παράσταση, το όνομα αρχείου εξόδου πρέπει να τελειώνει με \".html\" ή \".htm\"!",
            "88": "γραφικό κτίριο ...",
            "89": "φινίρισμα γραφικών!",
            "90": "Γραφήματα δοκιμής διείσδυσης",
            "91": "Αυτό το γράφημα δημιουργήθηκε από το OWASP Nettacker. Το γράφημα περιέχει όλες τις δραστηριότητες ενότητες, τον χάρτη δικτύου και τις ευαίσθητες πληροφορίες. Μην μοιραστείτε αυτό το αρχείο με οποιονδήποτε, αν δεν είναι αξιόπιστο.",
            "92": "Έκθεση OWASP Nettacker",
            "93": "Λεπτομέρειες λογισμικού: έκδοση OWASP Nettacker {0} [{1}] σε {2}",
            "94": "δεν βρέθηκαν ανοιχτές θύρες!",
            "95": "δεν βρέθηκε χρήστης / κωδικός πρόσβασης!",
            "96": "Έγινε φόρτωση {0} μονάδων ...",
            "97": "αυτό το στοιχείο γραφήματος δεν βρέθηκε: {0}",
            "98": "αυτή η ενότητα γραφικών \"{0}\" δεν είναι διαθέσιμη",
            "99": "ping πριν σαρώσετε τον κεντρικό υπολογιστή",
            "100": "παρακάμπτοντας ολόκληρο τον στόχο {0} και τη μέθοδο σάρωσης {1} εξαιτίας του -ping-before-scan είναι αλήθεια και δεν απάντησε!",
            "101": "δεν χρησιμοποιείτε την τελευταία έκδοση του OWASP Nettacker, ενημερώστε το.",
            "102": "δεν μπορείτε να ελέγξετε για την ενημέρωση, ελέγξτε τη σύνδεσή σας στο διαδίκτυο.",
            "103": "Χρησιμοποιείτε την τελευταία έκδοση του OWASP Nettacker ...",
            "104": "κατάλογο ευρετηρίου που βρέθηκε στο {0}",
            "105": "εισάγετε τη θύρα μέσω του διακόπτη -g ή -methods-args αντί της url",
            "106": "σύνδεση HTTP {0} timeout!",
            "107": "",
            "108": "δεν βρέθηκε κατάλογος ή αρχείο για {0} στη θύρα {1}",
            "109": "δεν μπορεί να ανοίξει {0}",
            "110": "Η τιμή dir_scan_http_method πρέπει να είναι GET ή HEAD, ορίστε προεπιλογή για GET.",
            "111": "λίστα όλων των μεθόδων args",
            "112": "δεν μπορεί να πάρει {0} args module",
            "113": "",
            "114": "",
            "115": "",
            "116": "",
            "117": ""
        }
