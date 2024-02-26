# Generated by Django 5.0.2 on 2024-02-20 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sb1010',
            fields=[
                ('b1_afamad', models.FloatField()),
                ('b1_filial', models.CharField(max_length=2)),
                ('b1_cod', models.CharField(max_length=15)),
                ('b1_desc', models.CharField(max_length=34)),
                ('b1_codite', models.CharField(max_length=27)),
                ('b1_tipo', models.CharField(max_length=2)),
                ('b1_um', models.CharField(max_length=2)),
                ('b1_descing', models.CharField(max_length=78)),
                ('b1_locpad', models.CharField(max_length=2)),
                ('b1_grupo', models.CharField(max_length=4)),
                ('b1_picm', models.FloatField()),
                ('b1_posipi', models.CharField(max_length=10)),
                ('b1_especie', models.CharField(max_length=2)),
                ('b1_ex_ncm', models.CharField(max_length=3)),
                ('b1_ex_nbm', models.CharField(max_length=3)),
                ('b1_ipi', models.FloatField()),
                ('b1_aliqiss', models.FloatField()),
                ('b1_codiss', models.CharField(max_length=9)),
                ('b1_te', models.CharField(max_length=3)),
                ('b1_ts', models.CharField(max_length=3)),
                ('b1_picmret', models.FloatField()),
                ('b1_picment', models.FloatField()),
                ('b1_bitmap', models.CharField(max_length=20)),
                ('b1_segum', models.CharField(max_length=2)),
                ('b1_impzfrc', models.CharField(max_length=1)),
                ('b1_conv', models.FloatField()),
                ('b1_tipconv', models.CharField(max_length=1)),
                ('b1_alter', models.CharField(max_length=15)),
                ('b1_qe', models.FloatField()),
                ('b1_prv1', models.FloatField()),
                ('b1_emin', models.FloatField()),
                ('b1_custd', models.FloatField()),
                ('b1_ucalstd', models.CharField(max_length=8)),
                ('b1_uprc', models.FloatField()),
                ('b1_ucom', models.CharField(max_length=8)),
                ('b1_mcustd', models.CharField(max_length=1)),
                ('b1_peso', models.FloatField()),
                ('b1_estfor', models.CharField(max_length=3)),
                ('b1_estseg', models.FloatField()),
                ('b1_forprz', models.CharField(max_length=3)),
                ('b1_pe', models.FloatField()),
                ('b1_tipe', models.CharField(max_length=1)),
                ('b1_le', models.FloatField()),
                ('b1_lm', models.FloatField()),
                ('b1_conta', models.CharField(max_length=20)),
                ('b1_toler', models.FloatField()),
                ('b1_cc', models.CharField(max_length=9)),
                ('b1_itemcc', models.CharField(max_length=9)),
                ('b1_familia', models.CharField(max_length=1)),
                ('b1_qb', models.FloatField()),
                ('b1_lojproc', models.CharField(max_length=2)),
                ('b1_proc', models.CharField(max_length=6)),
                ('b1_apropri', models.CharField(max_length=1)),
                ('b1_tipodec', models.CharField(max_length=1)),
                ('b1_origem', models.CharField(max_length=1)),
                ('b1_clasfis', models.CharField(max_length=2)),
                ('b1_fantasm', models.CharField(max_length=1)),
                ('b1_urev', models.CharField(max_length=8)),
                ('b1_datref', models.CharField(max_length=8)),
                ('b1_rastro', models.CharField(max_length=1)),
                ('b1_foraest', models.CharField(max_length=1)),
                ('b1_comis', models.FloatField()),
                ('b1_mono', models.CharField(max_length=1)),
                ('b1_dtrefp1', models.CharField(max_length=8)),
                ('b1_perinv', models.FloatField()),
                ('b1_grtrib', models.CharField(max_length=6)),
                ('b1_mrp', models.CharField(max_length=1)),
                ('b1_notamin', models.FloatField()),
                ('b1_prvalid', models.FloatField()),
                ('b1_conini', models.CharField(max_length=8)),
                ('b1_contsoc', models.CharField(max_length=1)),
                ('b1_numcop', models.FloatField()),
                ('b1_codbar', models.CharField(max_length=15)),
                ('b1_irrf', models.CharField(max_length=1)),
                ('b1_grade', models.CharField(max_length=1)),
                ('b1_formlot', models.CharField(max_length=3)),
                ('b1_fpcod', models.CharField(max_length=10)),
                ('b1_codgtin', models.CharField(max_length=15)),
                ('b1_localiz', models.CharField(max_length=1)),
                ('b1_desc_p', models.CharField(max_length=6)),
                ('b1_contrat', models.CharField(max_length=1)),
                ('b1_desc_gi', models.CharField(max_length=6)),
                ('b1_desc_i', models.CharField(max_length=6)),
                ('b1_operpad', models.CharField(max_length=2)),
                ('b1_vlrefus', models.FloatField()),
                ('b1_opc', models.CharField(max_length=80)),
                ('b1_anuente', models.CharField(max_length=1)),
                ('b1_codobs', models.CharField(max_length=6)),
                ('b1_import', models.CharField(max_length=1)),
                ('b1_fabric', models.CharField(max_length=20)),
                ('b1_sitprod', models.CharField(max_length=2)),
                ('b1_modelo', models.CharField(max_length=15)),
                ('b1_setor', models.CharField(max_length=2)),
                ('b1_balanca', models.CharField(max_length=1)),
                ('b1_prodpai', models.CharField(max_length=15)),
                ('b1_tecla', models.CharField(max_length=3)),
                ('b1_emax', models.FloatField()),
                ('b1_tipocq', models.CharField(max_length=1)),
                ('b1_solicit', models.CharField(max_length=1)),
                ('b1_quadpro', models.CharField(max_length=1)),
                ('b1_agregcu', models.CharField(max_length=1)),
                ('b1_base3', models.CharField(max_length=14)),
                ('b1_grupcom', models.CharField(max_length=6)),
                ('b1_despimp', models.CharField(max_length=1)),
                ('b1_desbse3', models.CharField(max_length=60)),
                ('b1_numcqpr', models.FloatField()),
                ('b1_contcqp', models.FloatField()),
                ('b1_pesbru', models.FloatField()),
                ('b1_observa', models.CharField(max_length=78)),
                ('b1_revatu', models.CharField(max_length=3)),
                ('b1_inss', models.CharField(max_length=1)),
                ('b1_codemb', models.CharField(max_length=30)),
                ('b1_especif', models.CharField(max_length=80)),
                ('b1_mat_pri', models.CharField(max_length=20)),
                ('b1_nalncca', models.CharField(max_length=7)),
                ('b1_redinss', models.FloatField()),
                ('b1_redirrf', models.FloatField()),
                ('b1_nalsh', models.CharField(max_length=8)),
                ('b1_aladi', models.CharField(max_length=3)),
                ('b1_tab_ipi', models.CharField(max_length=2)),
                ('b1_grudes', models.CharField(max_length=3)),
                ('b1_redpis', models.FloatField()),
                ('b1_redcof', models.FloatField()),
                ('b1_datasub', models.CharField(max_length=8)),
                ('b1_pcsll', models.FloatField()),
                ('b1_pcofins', models.FloatField()),
                ('b1_ppis', models.FloatField()),
                ('b1_mtbf', models.FloatField()),
                ('b1_mttr', models.FloatField()),
                ('b1_flagsug', models.CharField(max_length=1)),
                ('b1_classve', models.CharField(max_length=1)),
                ('b1_midia', models.CharField(max_length=1)),
                ('b1_qtmidia', models.FloatField()),
                ('b1_vlr_ipi', models.FloatField()),
                ('b1_envobr', models.CharField(max_length=1)),
                ('b1_qtdser', models.CharField(max_length=1)),
                ('b1_serie', models.CharField(max_length=20)),
                ('b1_faixas', models.FloatField()),
                ('b1_nropag', models.FloatField()),
                ('b1_isbn', models.CharField(max_length=10)),
                ('b1_titorig', models.CharField(max_length=50)),
                ('b1_lingua', models.CharField(max_length=20)),
                ('b1_edicao', models.CharField(max_length=3)),
                ('b1_obsisbn', models.CharField(max_length=40)),
                ('b1_clvl', models.CharField(max_length=9)),
                ('b1_ativo', models.CharField(max_length=1)),
                ('b1_tipcar', models.CharField(max_length=6)),
                ('b1_alfumac', models.FloatField()),
                ('b1_admin', models.CharField(max_length=10)),
                ('b1_ulocpd', models.CharField(max_length=2)),
                ('b1_qtdconf', models.FloatField()),
                ('b1_fracper', models.FloatField()),
                ('b1_int_icm', models.FloatField()),
                ('b1_vlr_icm', models.FloatField()),
                ('b1_vlrselo', models.FloatField()),
                ('b1_codnor', models.CharField(max_length=3)),
                ('b1_corpri', models.CharField(max_length=6)),
                ('b1_corsec', models.CharField(max_length=6)),
                ('b1_nicone', models.CharField(max_length=15)),
                ('b1_atrib1', models.CharField(max_length=6)),
                ('b1_atrib2', models.CharField(max_length=6)),
                ('b1_atrib3', models.CharField(max_length=6)),
                ('b1_regseq', models.CharField(max_length=6)),
                ('b1_cpotenc', models.CharField(max_length=1)),
                ('b1_potenci', models.FloatField()),
                ('b1_qtdacum', models.FloatField()),
                ('b1_qtdinic', models.FloatField()),
                ('b1_requis', models.CharField(max_length=1)),
                ('b1_selo', models.CharField(max_length=1)),
                ('b1_lotven', models.FloatField()),
                ('b1_ok', models.CharField(max_length=4)),
                ('b1_usafefo', models.CharField(max_length=1)),
                ('b1_iat', models.CharField(max_length=1)),
                ('b1_ippt', models.CharField(max_length=1)),
                ('b1_cnatrec', models.CharField(max_length=3)),
                ('b1_tnatrec', models.CharField(max_length=4)),
                ('b1_afasemt', models.FloatField()),
                ('b1_aimamt', models.FloatField()),
                ('b1_terum', models.CharField(max_length=2)),
                ('b1_afundes', models.FloatField()),
                ('b1_afabov', models.FloatField()),
                ('b1_cccusto', models.CharField(max_length=9)),
                ('b1_cest', models.CharField(max_length=9)),
                ('b1_chassi', models.CharField(max_length=25)),
                ('b1_classe', models.CharField(max_length=6)),
                ('b1_integ', models.CharField(max_length=1)),
                ('b1_hrexpo', models.CharField(max_length=8)),
                ('b1_markup', models.FloatField()),
                ('b1_mopc', models.BinaryField(blank=True, null=True)),
                ('b1_lotesbp', models.FloatField()),
                ('b1_msblql', models.CharField(max_length=1)),
                ('b1_pis', models.CharField(max_length=1)),
                ('b1_pmacnut', models.FloatField()),
                ('b1_pmicnut', models.FloatField()),
                ('b1_parcei', models.CharField(max_length=6)),
                ('b1_cricms', models.CharField(max_length=1)),
                ('b1_codproc', models.CharField(max_length=6)),
                ('b1_codqad', models.CharField(max_length=13)),
                ('b1_coefdcr', models.FloatField()),
                ('b1_dci', models.CharField(max_length=1)),
                ('b1_dcr', models.CharField(max_length=9)),
                ('b1_dcre', models.CharField(max_length=10)),
                ('b1_dcrii', models.FloatField()),
                ('b1_difcnae', models.CharField(max_length=11)),
                ('b1_dtcorte', models.CharField(max_length=8)),
                ('b1_dtfimnt', models.CharField(max_length=8)),
                ('b1_grpcst', models.CharField(max_length=3)),
                ('b1_grpnatr', models.CharField(max_length=2)),
                ('b1_fustf', models.CharField(max_length=1)),
                ('b1_gccusto', models.CharField(max_length=8)),
                ('b1_gdodif', models.CharField(max_length=1)),
                ('b1_escripi', models.CharField(max_length=1)),
                ('b1_fecp', models.FloatField()),
                ('b1_talla', models.CharField(max_length=6)),
                ('b1_tipobn', models.CharField(max_length=2)),
                ('b1_tpprod', models.CharField(max_length=2)),
                ('b1_tpreg', models.CharField(max_length=1)),
                ('b1_prodsbp', models.CharField(max_length=1)),
                ('b1_refbas', models.CharField(max_length=1)),
                ('b1_qbp', models.FloatField()),
                ('b1_userlga', models.CharField(max_length=17)),
                ('b1_userlgi', models.CharField(max_length=17)),
                ('b1_uvlrc', models.FloatField()),
                ('b1_valepre', models.CharField(max_length=1)),
                ('b1_verean', models.CharField(max_length=2)),
                ('b1_vigenc', models.CharField(max_length=8)),
                ('b1_vlcif', models.FloatField()),
                ('b1_umoec', models.FloatField()),
                ('b1_vlr_pis', models.FloatField()),
                ('b1_vlr_cof', models.FloatField()),
                ('b1_prodrec', models.CharField(max_length=1)),
                ('b1_pr43080', models.FloatField()),
                ('b1_prdori', models.CharField(max_length=15)),
                ('b1_prfdsul', models.FloatField()),
                ('b1_princmg', models.FloatField()),
                ('b1_prn944i', models.CharField(max_length=1)),
                ('b1_regesim', models.CharField(max_length=1)),
                ('b1_regriss', models.CharField(max_length=2)),
                ('b1_retoper', models.CharField(max_length=1)),
                ('b1_ricm65', models.CharField(max_length=1)),
                ('b1_rprodep', models.CharField(max_length=1)),
                ('b1_rsativo', models.CharField(max_length=1)),
                ('b1_tribmun', models.CharField(max_length=20)),
                ('b1_tpdp', models.CharField(max_length=1)),
                ('b1_tipvec', models.CharField(max_length=6)),
                ('b1_tfethab', models.CharField(max_length=1)),
                ('b1_seloen', models.CharField(max_length=6)),
                ('b1_sittrib', models.CharField(max_length=1)),
                ('b1_fecpba', models.FloatField()),
                ('b1_fethab', models.CharField(max_length=1)),
                ('b1_fecop', models.CharField(max_length=1)),
                ('b1_estrori', models.CharField(max_length=15)),
                ('b1_garant', models.CharField(max_length=1)),
                ('b1_grpti', models.CharField(max_length=4)),
                ('b1_fretiss', models.CharField(max_length=1)),
                ('b1_desbse2', models.CharField(max_length=60)),
                ('b1_cofins', models.CharField(max_length=1)),
                ('b1_color', models.CharField(max_length=10)),
                ('b1_cricmst', models.CharField(max_length=1)),
                ('b1_csll', models.CharField(max_length=1)),
                ('b1_crdest', models.FloatField()),
                ('b1_crdpres', models.FloatField()),
                ('b1_pautfet', models.FloatField()),
                ('b1_pafmd5', models.CharField(max_length=32)),
                ('b1_pergart', models.FloatField()),
                ('b1_porcprl', models.CharField(max_length=2)),
                ('b1_msexp', models.CharField(max_length=8)),
                ('b1_ivaaju', models.CharField(max_length=1)),
                ('b1_meples', models.CharField(max_length=1)),
                ('b1_idhist', models.CharField(max_length=20)),
                ('b1_impncm', models.FloatField()),
                ('b1_cnae', models.CharField(max_length=9)),
                ('b1_codant', models.CharField(max_length=15)),
                ('b1_codlan', models.CharField(max_length=6)),
                ('b1_cfem', models.CharField(max_length=1)),
                ('b1_cfema', models.FloatField()),
                ('b1_cfems', models.CharField(max_length=1)),
                ('b1_base', models.CharField(max_length=14)),
                ('b1_base2', models.CharField(max_length=14)),
                ('b1_calcfet', models.CharField(max_length=1)),
                ('b1_cargae', models.CharField(max_length=1)),
                ('b1_ajudif', models.CharField(max_length=1)),
                ('b1_afacs', models.FloatField()),
                ('b1_afethab', models.FloatField()),
                ('b1_alfecop', models.FloatField()),
                ('b1_alfecrn', models.FloatField()),
                ('b1_alfecst', models.FloatField()),
                ('b1_ccpcp', models.CharField(max_length=9)),
                ('b1_dtconf', models.CharField(max_length=8)),
                ('d_e_l_e_t_field', models.CharField(db_column='d_e_l_e_t_', max_length=1)),
                ('r_e_c_n_o_field', models.BigIntegerField(db_column='r_e_c_n_o_', primary_key=True, serialize=False)),
                ('r_e_c_d_e_l_field', models.BigIntegerField(db_column='r_e_c_d_e_l_')),
                ('b1_tempo', models.FloatField()),
            ],
            options={
                'db_table': 'sb1010',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sd3010',
            fields=[
                ('d3_filial', models.CharField(max_length=2)),
                ('d3_tm', models.CharField(max_length=3)),
                ('d3_cod', models.CharField(max_length=15)),
                ('d3_um', models.CharField(max_length=2)),
                ('d3_quant', models.FloatField()),
                ('d3_cf', models.CharField(max_length=3)),
                ('d3_conta', models.CharField(max_length=20)),
                ('d3_op', models.CharField(max_length=14)),
                ('d3_local', models.CharField(max_length=2)),
                ('d3_doc', models.CharField(max_length=9)),
                ('d3_emissao', models.CharField(max_length=8)),
                ('d3_grupo', models.CharField(max_length=4)),
                ('d3_custo1', models.FloatField()),
                ('d3_custo2', models.FloatField()),
                ('d3_custo3', models.FloatField()),
                ('d3_custo4', models.FloatField()),
                ('d3_custo5', models.FloatField()),
                ('d3_cc', models.CharField(max_length=9)),
                ('d3_parctot', models.CharField(max_length=1)),
                ('d3_estorno', models.CharField(max_length=1)),
                ('d3_numseq', models.CharField(max_length=6)),
                ('d3_segum', models.CharField(max_length=2)),
                ('d3_qtsegum', models.FloatField()),
                ('d3_tipo', models.CharField(max_length=2)),
                ('d3_nivel', models.CharField(max_length=3)),
                ('d3_usuario', models.CharField(max_length=25)),
                ('d3_regwms', models.CharField(max_length=1)),
                ('d3_perda', models.FloatField()),
                ('d3_dtlanc', models.CharField(max_length=8)),
                ('d3_trt', models.CharField(max_length=3)),
                ('d3_chave', models.CharField(max_length=2)),
                ('d3_ident', models.CharField(max_length=6)),
                ('d3_seqcalc', models.CharField(max_length=14)),
                ('d3_rateio', models.FloatField()),
                ('d3_lotectl', models.CharField(max_length=10)),
                ('d3_numlote', models.CharField(max_length=6)),
                ('d3_dtvalid', models.CharField(max_length=8)),
                ('d3_localiz', models.CharField(max_length=15)),
                ('d3_numseri', models.CharField(max_length=20)),
                ('d3_cusff1', models.FloatField()),
                ('d3_cusff2', models.FloatField()),
                ('d3_cusff3', models.FloatField()),
                ('d3_cusff4', models.FloatField()),
                ('d3_cusff5', models.FloatField()),
                ('d3_item', models.CharField(max_length=2)),
                ('d3_ok', models.CharField(max_length=2)),
                ('d3_itemcta', models.CharField(max_length=9)),
                ('d3_clvl', models.CharField(max_length=9)),
                ('d3_projpms', models.CharField(max_length=10)),
                ('d3_taskpms', models.CharField(max_length=12)),
                ('d3_ordem', models.CharField(max_length=6)),
                ('d3_servic', models.CharField(max_length=3)),
                ('d3_stserv', models.CharField(max_length=1)),
                ('d3_ostec', models.CharField(max_length=8)),
                ('d3_potenci', models.FloatField()),
                ('d3_tpestr', models.CharField(max_length=6)),
                ('d3_regaten', models.CharField(max_length=10)),
                ('d3_docswn', models.CharField(max_length=15)),
                ('d3_itemswn', models.CharField(max_length=4)),
                ('d3_itemgrd', models.CharField(max_length=3)),
                ('d3_status', models.CharField(max_length=2)),
                ('d3_cusrp1', models.FloatField()),
                ('d3_cusrp2', models.FloatField()),
                ('d3_cusrp3', models.FloatField()),
                ('d3_cusrp4', models.FloatField()),
                ('d3_cusrp5', models.FloatField()),
                ('d3_cmrp', models.FloatField()),
                ('d3_moedrp', models.CharField(max_length=1)),
                ('d3_revisao', models.CharField(max_length=3)),
                ('d3_tanque', models.CharField(max_length=6)),
                ('d3_massa', models.FloatField()),
                ('d3_tempamo', models.FloatField()),
                ('d3_temptaq', models.FloatField()),
                ('d3_densamb', models.FloatField()),
                ('d3_qtdamb', models.FloatField()),
                ('d3_fatcorr', models.FloatField()),
                ('d3_tpmovaj', models.CharField(max_length=2)),
                ('d3_codfor', models.CharField(max_length=6)),
                ('d3_lojafor', models.CharField(max_length=2)),
                ('d3_nforp', models.CharField(max_length=6)),
                ('d3_obs', models.CharField(max_length=20)),
                ('d3_chavef2', models.CharField(max_length=52)),
                ('d3_hawb', models.CharField(max_length=17)),
                ('d3_iddcf', models.CharField(max_length=6)),
                ('d3_lojadoc', models.CharField(max_length=2)),
                ('d3_moeda', models.CharField(max_length=1)),
                ('d3_forndoc', models.CharField(max_length=6)),
                ('d3_garanti', models.CharField(max_length=1)),
                ('d3_diactb', models.CharField(max_length=2)),
                ('d3_empop', models.CharField(max_length=1)),
                ('d3_cmfixo', models.FloatField()),
                ('d3_chavef1', models.CharField(max_length=52)),
                ('d3_numsa', models.CharField(max_length=6)),
                ('d3_nodia', models.CharField(max_length=10)),
                ('d3_nrabate', models.CharField(max_length=8)),
                ('d3_nrbpims', models.CharField(max_length=10)),
                ('d3_qtganho', models.FloatField()),
                ('d3_qtmaior', models.FloatField()),
                ('d3_perimp', models.FloatField()),
                ('d3_pmacnut', models.FloatField()),
                ('d3_pmicnut', models.FloatField()),
                ('d3_perblk', models.CharField(max_length=6)),
                ('d3_vlrvi', models.FloatField()),
                ('d3_vlrpd', models.FloatField()),
                ('d3_teatf', models.CharField(max_length=3)),
                ('d3_observa', models.CharField(max_length=30)),
                ('d3_okiss', models.CharField(max_length=2)),
                ('d3_codlan', models.CharField(max_length=6)),
                ('d3_codsaf', models.CharField(max_length=15)),
                ('d3_father', models.CharField(max_length=1)),
                ('d3_itemsa', models.CharField(max_length=2)),
                ('d_e_l_e_t_field', models.CharField(db_column='d_e_l_e_t_', max_length=1)),
                ('r_e_c_n_o_field', models.BigIntegerField(db_column='r_e_c_n_o_', primary_key=True, serialize=False)),
                ('r_e_c_d_e_l_field', models.BigIntegerField(db_column='r_e_c_d_e_l_')),
                ('d3_loteprt', models.CharField(max_length=10)),
                ('d3_dtinipd', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'sd3010',
                'managed': False,
            },
        ),
    ]