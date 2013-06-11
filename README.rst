VFDB
====

The virulence factor/regions of interest databases used in the ST131 project.

MANIFEST:
    * ALL_FEATURES.fa (concatenation of all unique features)
    * Antibiotics.fa (bla-CTX-M-1 for CTX-15)
    * Antibiotics_CTX-15.fa
    * Autotransporters.fa
    * Colicins_and_microcins.fa
    * CU_fimbriae.fa
    * fimB.fa (wt and IS)
    * Iron_uptake.fa
    * Islands.fa (not if SeqFindR format, use chunk_mfa.py)
    * Islands_500bp_chunks.fa
    * O_antigen.fa (from Islands.fa)
    * Other_virulence_genes.fa
    * plasmid_replicons.fa
    * Schembri_VFDB.fa (Autotransporters, Colicins_and_microcins, CU_fimbriae,
      Iron_uptake, Other_virulence_genes, Toxins, UPEC_specific_genes)
    * Toxins.fa
    * UPEC_specific_genes.fa

The following were duplicates across the pooled database:
    * c0393
    * c4308
    * c3610
    * c3619
    * c2436
    * c1374
    * c2482
    * c2775

**On the 07/06/2013 Mat Upton pointed out that there was an issues with some
sequences in the database. This was due to a bug in the KEGG extract script.**

The following databases are not effected:
    * Antibiotics.fa & Antibiotics_CTX-15.fa
    * fimB.fa
    * Islands.fa
    * Islands_500bp_chunks.fa
    * O_antigen.fa
    * plasmid_replicons.fa
