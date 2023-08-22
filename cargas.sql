/*>>>>Banco TMCorpapp<<<<*/
use tmcorp;

/*>>>>Encontrar as tabelas do DB<<<<*/
SELECT * FROM information_schema.tables where table_schema in (SELECT  DATABASE ());

/*>>>>Tabelas TMCorpapp<<<<
- auth_group
- auth_group_permissions
- auth_permission
- django_admin_log
- django_content_type
- django_migrations
- django_session
- tmglobal_clientes
- tmglobal_empresas
- tmglobal_fornecedores
- tmglobal_noc_global_choices
- tmglobal_users
- tmglobal_users_groups
- tmglobal_users_user_permissions
- tmrat_noc_rat_choices
- tmrat_relattec
*/

/*>>>>Campos das Tabelas<<<<

DESC tmglobal_clientes
cod_cli
seq_cli
tp_cli
nm_jur_cli
nm_com_cli
tel_cli
cnpj_cpf_cli
end_cli
end_compl_cli
end_bairro_cli
end_cidade_cli
end_cep_cli
end_uf_cli
dt_ini_relac_cli


DESC tmglobal_empresas
empresas_pk
cod_empresa
cod_filial
nome_empresa
nome_filial
nome_comercial
telefone
cnpj
endereco
end_complemento
end_bairro
end_cidade
end_cep
end_uf
cnae
lic_licenca
lic_chave
lic_checksum
lic_validade

DESC tmglobal_fornecedores
cod_for
seq_for
tp_for
nm_jur_for
nm_com_for
tel_for
cnpj_cpf_for
end_for
end_compl_for
end_bairro_for
end_cidade_for
end_cep_for
end_uf_for
dt_ini_relac_for

DESC tmglobal_users
id
password
last_login
is_superuser
username
first_name
last_name
email
is_staff
is_active
date_joined
usr_empresa
usr_filial
usr_cargo

/*Insert tmrat_relattec
DESC tmrat_relattec (encontrar nome dos campos)

INSERT INTO tmrat_relattec(rat_pk, tp_rat,dt_rat,hr_ini_rat,vl_atend_rat,probl_rat,desc_rat,conclusao_rat,desc_pecas_rat,hr_fim_rat,vl_pecas_rat) 
VALUES(1,'C','2023-07-28','14:16:16',11.00,'Problema encontrado no computador','Foi diagnosticado problema  ','Vamos arrumar o ','Peças usadas:Memoria, HD',          '16:18:10',10.00);

INSERT INTO tmrat_relattec(rat_pk, tp_rat,dt_rat,hr_ini_rat,vl_atend_rat,probl_rat,desc_rat,conclusao_rat,desc_pecas_rat,hr_fim_rat,vl_pecas_rat) 
VALUES(2,'A','2023-06-23','15:15:11',13.00,'Problema encontrado na impressora','Foi diagnosticado problema  ','Vamos arrumar o computador','Peças usadas:Memoria, HD','16:18:10',10.00);

INSERT INTO tmrat_relattec(rat_pk, tp_rat,dt_rat,hr_ini_rat,vl_atend_rat,probl_rat,desc_rat,conclusao_rat,desc_pecas_rat,hr_fim_rat,vl_pecas_rat) 
VALUES(3,'G','2023-05-14','08:13:12',12.00,'Problema encontrado na televisão','Foi diagnosticado problema  ','Vamos arrumar o ','Peças usadas:Memoria, HD',			  '09:18:10',10.00);

INSERT INTO tmrat_relattec(rat_pk, tp_rat,dt_rat,hr_ini_rat,vl_atend_rat,probl_rat,desc_rat,conclusao_rat,desc_pecas_rat,hr_fim_rat,vl_pecas_rat) 
VALUES(4,'G','2023-04-12','08:12:53',12.00,'Problema encontrado no maquina','Foi diagnosticado problema  ','Vamos arrumar o computador','Peças usadas:Memoria, HD',   '09:18:10',10.00);

INSERT INTO tmrat_relattec(rat_pk, tp_rat,dt_rat,hr_ini_rat,vl_atend_rat,probl_rat,desc_rat,conclusao_rat,desc_pecas_rat,hr_fim_rat,vl_pecas_rat) VALUES(5,'A','2023-07-25','09:32:56',05.00,'Problema encontrado no material','Foi diagnosticado problema  ','Vamos arrumar o ','Peças usadas:Memoria, HD',            '10:18:10',10.00);
VALUES(6,'C','2023-07-30','11:43:54',06.00,'Problema encontrado no loren','Foi diagnosticado problema  ','Vamos arrumar o ','Peças usadas:Memoria, HD',               '13:18:10',10.00);

INSERT INTO tmrat_relattec(rat_pk, tp_rat,dt_rat,hr_ini_rat,vl_atend_rat,probl_rat,desc_rat,conclusao_rat,desc_pecas_rat,hr_fim_rat,vl_pecas_rat) VALUES(7,'A','2023-07-31','12:55:45',15.00,'Problema encontrado no compras','Foi diagnosticado problema  ','Vamos arrumar o ','Peças usadas:Memoria, HD',             '13:18:10',10.00);
VALUES(8,'C','2023-07-23','12:56:34',18.00,'Problema encontrado no favsicn','Foi diagnosticado problema  ','Vamos arrumar o ','Peças usadas:Memoria, HD',             '13:18:10',10.00);

INSERT INTO tmrat_relattec(rat_pk, tp_rat,dt_rat,hr_ini_rat,vl_atend_rat,probl_rat,desc_rat,conclusao_rat,desc_pecas_rat,hr_fim_rat,vl_pecas_rat) VALUES(9,'C','2023-07-14','13:34:32',22.00,'Problema encontrado no compras','Foi diagnosticado problema  ','Vamos arrumar o ','Peças usadas:Memoria, HD',             '14:18:10',10.00);
VALUES(10,'G','2023-07-14','16:33:34',22.00,'Problema encontrado no jovem','Foi diagnosticado problema  ','Vamos arrumar o ','Peças usadas:Memoria, HD',              '17:18:10',10.00);

INSERT INTO tmrat_relattec(rat_pk, tp_rat,dt_rat,hr_ini_rat,vl_atend_rat,probl_rat,desc_rat,conclusao_rat,desc_pecas_rat,hr_fim_rat,vl_pecas_rat) VALUES(11,'C','2023-07-24','17:16:44',25.00,'Problema encontrado no loren 2','Foi diagnosticado problema  ','Vamos arrumar o ','Peças usadas:Memoria, HD',            '18:18:10',10.00);
VALUES(12,'A','2023-07-25','14:23:44',43.00,'Problema encontrado no super','Foi diagnosticado problema  ','Vamos arrumar o ','Peças usadas:Memoria, HD',              '15:18:10',10.00);

INSERT INTO tmrat_relattec(rat_pk, tp_rat,dt_rat,hr_ini_rat,vl_atend_rat,probl_rat,desc_rat,conclusao_rat,desc_pecas_rat,hr_fim_rat,vl_pecas_rat) VALUES(13,'C','2023-07-24','15:14:24',42.00,'Problema encontrado no autonomo','Foi diagnosticado problema  ','Vamos arrumar o ','Peças usadas:Memoria, HD',           '16:18:10',10.00);
VALUES(14,'C','2023-07-23','07:16:32',34.00,'Problema encontrado no matricula','Foi diagnosticado problema  ','Vamos arrumar o ','Peças usadas:Memoria, HD',          '07:18:10',10.00);

INSERT INTO tmrat_relattec(rat_pk, tp_rat,dt_rat,hr_ini_rat,vl_atend_rat,probl_rat,desc_rat,conclusao_rat,desc_pecas_rat,hr_fim_rat,vl_pecas_rat) 
VALUES(15,'C','2023-07-28','06:16:33',10.00,'Problema encontrado no apere','Foi diagnosticado problema  ','Vamos arrumar o ','Peças usadas:Memoria, HD',              '08:18:10',10.00);
*/
