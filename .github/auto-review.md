# Règles de relecture — Skills-accessibilite

Écosystème de skills comportementaux pour LLM (aucun code applicatif) : le
livrable est le texte des `SKILL.md`, qui programme la manière dont un
modèle s'adresse à des personnes avec des besoins cognitifs, sensoriels ou
neurobiologiques spécifiques. Une régression ici est un changement de
comportement du modèle envers un public vulnérable, pas un bug logiciel.

## À vérifier en priorité, dans cet ordre

1. **Déclencheurs qui infèrent au lieu de déclarer.** Un skill
   d'accessibilité doit s'activer sur déclaration explicite ou besoin
   formulé directement — jamais à partir de signaux faibles (fautes
   d'orthographe, mention de fatigue ordinaire, procrastination, style
   d'écriture). Une modification de `description` (frontmatter) ou d'une
   section « déclencheur » qui élargit implicitement l'activation à ces
   signaux est une régression, même si `validate_skills.py` reste vert (il
   ne vérifie que la présence et la longueur du champ, pas son contenu).
2. **Essentialisation.** Toute formulation qui impute un trait, un
   comportement ou un ressenti à une catégorie de personnes (« les
   autistes… », « avec ton TDAH… ») plutôt qu'à la personne elle-même.
3. **Glissement forme → fond.** Les skills d'accessibilité doivent changer
   la manière de répondre, jamais l'exactitude ni la complétude du
   contenu. Un ajout qui ferait taire, édulcorer ou biaiser une information
   factuelle au nom de l'accessibilité est à signaler.
4. **Affaiblissement de la sécurité éthique.** Toute modification de
   `psychologie-rigoureuse` ou de `docs/note_ethique.md` qui réduirait la
   priorité de l'orientation vers un soutien professionnel face à une
   souffrance durable ou un risque.
5. **Bloc « Ordre de préséance » modifié dans un seul `SKILL.md`.**
   `validate_skills.py` détecte déjà la divergence de hash entre les 7
   fichiers, mais pas une PR qui modifie le bloc dans les 7 à la fois de
   façon substantiellement différente de `AGENTS.md` (qui documente
   l'ordre canonique) — la cohérence texte-documentation reste à
   vérifier humainement.
6. **Incohérence de version entre `SKILL.md`, `README.md` et
   `docs/index_skills.md`.** Rien ne vérifie automatiquement qu'un bump de
   version (`V<major>.<minor>`) dans le frontmatter d'un skill est
   répercuté dans le tableau du README et dans l'index canonique.
7. **`CHANGELOG.md` non mis à jour** pour un changement de comportement
   notable d'un skill (format Keep a Changelog, section `[Non publié]`).
8. **Preuves de vague d'évaluation non assainies.** Une promotion de skill
   doit s'accompagner d'un paquet sous `eval/evidence/<horodatage>/` ; la
   CI vérifie sa présence et sa structure mais pas son contenu — vérifier
   qu'aucune donnée personnelle identifiable ne subsiste dans les cas
   d'évaluation ou les verbatims cités, et que `blinding_map.json` (qui
   lève l'anonymat des juges) n'est pas commité par erreur.

## À ne pas signaler

Déjà couvert par `scripts/validate_skills.py` (CI `validate.yml`), inutile
de le répéter :
- Frontmatter YAML absent, `name` différent du nom du dossier,
  `description` de plus de 1024 caractères, valeur de frontmatter qui
  casserait un parseur YAML strict.
- Fichier `SKILL.md` de 500 lignes ou plus.
- Bloc « Ordre de préséance » absent d'un skill, ou divergent par hash
  entre les 7 fichiers (déjà détecté par comparaison sha256).
