-- enrutador.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad de enrutador
entity enrutador is
	generic(
		N : natural := 3;
		N_SEM : natural := 3;
		N_PAN : natural := 1;
		N_MDC : natural := 2;
		N_RUT : natural := 3
	);
	port(
		Clock : in std_logic;
		Reset : in std_logic;
		CV_int_Ruta_1 : in std_logic;
		CV_paralelo_Ruta_1 : in std_logic_vector(2-1 downto 0);
		CV_paralelo_temp_Ruta_1 : in std_logic_vector(3-1 downto 0);
		CV_despeje_Ruta_1 : in std_logic_vector(4-1 downto 0);
		CV_aprox_Ruta_1 : in std_logic_vector(5-1 downto 0);
		Estado_sub_ruta_Ruta_1 : in std_logic_vector(6-1 downto 0);
		Estado_ruta_cond_Ruta_1 : in std_logic_vector(7-1 downto 0);
		Estado_ruta_confl_Ruta_1 : in std_logic_vector(8-1 downto 0);
		Estado_SEM_sgte_Ruta_1 : in std_logic_vector(9-1 downto 0);
		Pos_MDC_ruta_Ruta_1 : in std_logic_vector(10-1 downto 0);
		Pos_MDC_aprox_Ruta_1 : in std_logic_vector(11-1 downto 0);
		Pos_MDC_despeje_Ruta_1 : in std_logic_vector(12-1 downto 0);
		Pos_MDC_solape_Ruta_1 : in std_logic_vector(13-1 downto 0);
		Bloq_MDC_ruta_Ruta_1 : in std_logic_vector(14-1 downto 0);
		Bloq_MDC_solape_Ruta_1 : in std_logic_vector(15-1 downto 0);
		Estado_PAN_Ruta_1 : in std_logic_vector(16-1 downto 0);
		Estado_CV_bloq_Ruta_1 : in std_logic;
		Estado_ruta_bloq_Ruta_1 : in std_logic_vector(18-1 downto 0);
		MDC_bloq_temp_solape_Ruta_1 : in std_logic_vector(19-1 downto 0);
		Estado_ruta_Ruta_1 : in std_logic_vector(20-1 downto 0);
		CV_alarma_total_Ruta_1 : in std_logic_vector(21-1 downto 0);
		CV_alarma_inmediata_Ruta_1 : in std_logic_vector(22-1 downto 0);
		PAN_bloq_temp_solape_Ruta_1 : in std_logic_vector(23-1 downto 0);
		CV_int_Ruta_2 : in std_logic;
		CV_paralelo_Ruta_2 : in std_logic_vector(2-1 downto 0);
		CV_paralelo_temp_Ruta_2 : in std_logic_vector(3-1 downto 0);
		CV_despeje_Ruta_2 : in std_logic_vector(4-1 downto 0);
		CV_aprox_Ruta_2 : in std_logic_vector(5-1 downto 0);
		Estado_sub_ruta_Ruta_2 : in std_logic_vector(6-1 downto 0);
		Estado_ruta_cond_Ruta_2 : in std_logic_vector(7-1 downto 0);
		Estado_ruta_confl_Ruta_2 : in std_logic_vector(8-1 downto 0);
		Estado_SEM_sgte_Ruta_2 : in std_logic_vector(9-1 downto 0);
		Pos_MDC_ruta_Ruta_2 : in std_logic_vector(10-1 downto 0);
		Pos_MDC_aprox_Ruta_2 : in std_logic_vector(11-1 downto 0);
		Pos_MDC_despeje_Ruta_2 : in std_logic_vector(12-1 downto 0);
		Pos_MDC_solape_Ruta_2 : in std_logic_vector(13-1 downto 0);
		Bloq_MDC_ruta_Ruta_2 : in std_logic_vector(14-1 downto 0);
		Bloq_MDC_solape_Ruta_2 : in std_logic_vector(15-1 downto 0);
		Estado_PAN_Ruta_2 : in std_logic_vector(16-1 downto 0);
		Estado_CV_bloq_Ruta_2 : in std_logic;
		Estado_ruta_bloq_Ruta_2 : in std_logic_vector(18-1 downto 0);
		MDC_bloq_temp_solape_Ruta_2 : in std_logic_vector(19-1 downto 0);
		Estado_ruta_Ruta_2 : in std_logic_vector(20-1 downto 0);
		CV_alarma_total_Ruta_2 : in std_logic_vector(21-1 downto 0);
		CV_alarma_inmediata_Ruta_2 : in std_logic_vector(22-1 downto 0);
		PAN_bloq_temp_solape_Ruta_2 : in std_logic_vector(23-1 downto 0);
		CV_int_Ruta_3 : in std_logic;
		CV_paralelo_Ruta_3 : in std_logic_vector(2-1 downto 0);
		CV_paralelo_temp_Ruta_3 : in std_logic_vector(3-1 downto 0);
		CV_despeje_Ruta_3 : in std_logic_vector(4-1 downto 0);
		CV_aprox_Ruta_3 : in std_logic_vector(5-1 downto 0);
		Estado_sub_ruta_Ruta_3 : in std_logic_vector(6-1 downto 0);
		Estado_ruta_cond_Ruta_3 : in std_logic_vector(7-1 downto 0);
		Estado_ruta_confl_Ruta_3 : in std_logic_vector(8-1 downto 0);
		Estado_SEM_sgte_Ruta_3 : in std_logic_vector(9-1 downto 0);
		Pos_MDC_ruta_Ruta_3 : in std_logic_vector(10-1 downto 0);
		Pos_MDC_aprox_Ruta_3 : in std_logic_vector(11-1 downto 0);
		Pos_MDC_despeje_Ruta_3 : in std_logic_vector(12-1 downto 0);
		Pos_MDC_solape_Ruta_3 : in std_logic_vector(13-1 downto 0);
		Bloq_MDC_ruta_Ruta_3 : in std_logic_vector(14-1 downto 0);
		Bloq_MDC_solape_Ruta_3 : in std_logic_vector(15-1 downto 0);
		Estado_PAN_Ruta_3 : in std_logic_vector(16-1 downto 0);
		Estado_CV_bloq_Ruta_3 : in std_logic;
		Estado_ruta_bloq_Ruta_3 : in std_logic_vector(18-1 downto 0);
		MDC_bloq_temp_solape_Ruta_3 : in std_logic_vector(19-1 downto 0);
		Estado_ruta_Ruta_3 : in std_logic_vector(20-1 downto 0);
		CV_alarma_total_Ruta_3 : in std_logic_vector(21-1 downto 0);
		CV_alarma_inmediata_Ruta_3 : in std_logic_vector(22-1 downto 0);
		PAN_bloq_temp_solape_Ruta_3 : in std_logic_vector(23-1 downto 0);
		SEM_rojo_Ruta_1 : out std_logic;
		SEM_naranja_Ruta_1 : out std_logic;
		SEM_doble_naranja_Ruta_1 : out std_logic;
		SEM_verde_Ruta_1 : out std_logic;
		MDC_normal_Ruta_1 : out std_logic;
		MDC_reverso_Ruta_1 : out std_logic;
		MDC_libre_Ruta_1 : out std_logic;
		MDC_cerrojado_Ruta_1 : out std_logic;
		PAN_alto_Ruta_1 : out std_logic;
		PAN_bajo_Ruta_1 : out std_logic;
		PAN_alarma_Ruta_1 : out std_logic;
		PAN_habilitacion_Ruta_1 : out std_logic;
		RUT_estado_Ruta_1 : out std_logic;
		RUT_sem_bloq_slp_Ruta_1 : out std_logic;
		SEM_rojo_Ruta_2 : out std_logic;
		SEM_naranja_Ruta_2 : out std_logic;
		SEM_doble_naranja_Ruta_2 : out std_logic;
		SEM_verde_Ruta_2 : out std_logic;
		MDC_normal_Ruta_2 : out std_logic;
		MDC_reverso_Ruta_2 : out std_logic;
		MDC_libre_Ruta_2 : out std_logic;
		MDC_cerrojado_Ruta_2 : out std_logic;
		PAN_alto_Ruta_2 : out std_logic;
		PAN_bajo_Ruta_2 : out std_logic;
		PAN_alarma_Ruta_2 : out std_logic;
		PAN_habilitacion_Ruta_2 : out std_logic;
		RUT_estado_Ruta_2 : out std_logic;
		RUT_sem_bloq_slp_Ruta_2 : out std_logic;
		SEM_rojo_Ruta_3 : out std_logic;
		SEM_naranja_Ruta_3 : out std_logic;
		SEM_doble_naranja_Ruta_3 : out std_logic;
		SEM_verde_Ruta_3 : out std_logic;
		MDC_normal_Ruta_3 : out std_logic;
		MDC_reverso_Ruta_3 : out std_logic;
		MDC_libre_Ruta_3 : out std_logic;
		MDC_cerrojado_Ruta_3 : out std_logic;
		PAN_alto_Ruta_3 : out std_logic;
		PAN_bajo_Ruta_3 : out std_logic;
		PAN_alarma_Ruta_3 : out std_logic;
		PAN_habilitacion_Ruta_3 : out std_logic;
		RUT_estado_Ruta_3 : out std_logic;
		RUT_sem_bloq_slp_Ruta_3 : out std_logic
	);
end entity enrutador;
-- Arquitectura del enrutador : Descripcion del comportamiento
architecture enrutador_ARQ of enrutador is
	--componente_1 de mdc_fsm
	component mdc_fsm_1 is
		generic(
			N_RUT : natural := 3;
			N_SEM : natural := 3
		);
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			Estado_CV_bloq_Ruta_1 : in std_logic;
			Estado_ruta_bloq_Ruta_1 : in std_logic_vector(18-1 downto 0);
			MDC_bloq_temp_solape_Ruta_1 : in std_logic_vector(19-1 downto 0);
			MDC_normal_Ruta_1 : out std_logic;
			MDC_reverso_Ruta_1 : out std_logic;
			MDC_libre_Ruta_1 : out std_logic;
			MDC_cerrojado_Ruta_1 : out std_logic
		);
	end component mdc_fsm_1;
	--componente_2 de mdc_fsm
	component mdc_fsm_2 is
		generic(
			N_RUT : natural := 3;
			N_SEM : natural := 3
		);
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			Estado_CV_bloq_Ruta_2 : in std_logic;
			Estado_ruta_bloq_Ruta_2 : in std_logic_vector(18-1 downto 0);
			MDC_bloq_temp_solape_Ruta_2 : in std_logic_vector(19-1 downto 0);
			MDC_normal_Ruta_2 : out std_logic;
			MDC_reverso_Ruta_2 : out std_logic;
			MDC_libre_Ruta_2 : out std_logic;
			MDC_cerrojado_Ruta_2 : out std_logic
		);
	end component mdc_fsm_2;
	--componente_3 de mdc_fsm
	component mdc_fsm_3 is
		generic(
			N_RUT : natural := 3;
			N_SEM : natural := 3
		);
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			Estado_CV_bloq_Ruta_3 : in std_logic;
			Estado_ruta_bloq_Ruta_3 : in std_logic_vector(18-1 downto 0);
			MDC_bloq_temp_solape_Ruta_3 : in std_logic_vector(19-1 downto 0);
			MDC_normal_Ruta_3 : out std_logic;
			MDC_reverso_Ruta_3 : out std_logic;
			MDC_libre_Ruta_3 : out std_logic;
			MDC_cerrojado_Ruta_3 : out std_logic
		);
	end component mdc_fsm_3;
	--componente_1 de pan_fsm
	component pan_fsm_1 is
		generic(
			N_RUT : natural := 3;
			N_SEM : natural := 3
		);
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			Estado_ruta_Ruta_1 : in std_logic_vector(20-1 downto 0);
			CV_alarma_total_Ruta_1 : in std_logic_vector(21-1 downto 0);
			CV_alarma_inmediata_Ruta_1 : in std_logic_vector(22-1 downto 0);
			PAN_bloq_temp_solape_Ruta_1 : in std_logic_vector(23-1 downto 0);
			PAN_alto_Ruta_1 : out std_logic;
			PAN_bajo_Ruta_1 : out std_logic;
			PAN_alarma_Ruta_1 : out std_logic;
			PAN_habilitacion_Ruta_1 : out std_logic
		);
	end component pan_fsm_1;
	--componente_2 de pan_fsm
	component pan_fsm_2 is
		generic(
			N_RUT : natural := 3;
			N_SEM : natural := 3
		);
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			Estado_ruta_Ruta_2 : in std_logic_vector(20-1 downto 0);
			CV_alarma_total_Ruta_2 : in std_logic_vector(21-1 downto 0);
			CV_alarma_inmediata_Ruta_2 : in std_logic_vector(22-1 downto 0);
			PAN_bloq_temp_solape_Ruta_2 : in std_logic_vector(23-1 downto 0);
			PAN_alto_Ruta_2 : out std_logic;
			PAN_bajo_Ruta_2 : out std_logic;
			PAN_alarma_Ruta_2 : out std_logic;
			PAN_habilitacion_Ruta_2 : out std_logic
		);
	end component pan_fsm_2;
	--componente_3 de pan_fsm
	component pan_fsm_3 is
		generic(
			N_RUT : natural := 3;
			N_SEM : natural := 3
		);
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			Estado_ruta_Ruta_3 : in std_logic_vector(20-1 downto 0);
			CV_alarma_total_Ruta_3 : in std_logic_vector(21-1 downto 0);
			CV_alarma_inmediata_Ruta_3 : in std_logic_vector(22-1 downto 0);
			PAN_bloq_temp_solape_Ruta_3 : in std_logic_vector(23-1 downto 0);
			PAN_alto_Ruta_3 : out std_logic;
			PAN_bajo_Ruta_3 : out std_logic;
			PAN_alarma_Ruta_3 : out std_logic;
			PAN_habilitacion_Ruta_3 : out std_logic
		);
	end component pan_fsm_3;
	--componente_1 de sem_fsm
	component sem_fsm_1 is
		generic(
			N_RUT : natural := 3;
			N_SEM : natural := 3
		);
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			SEM_estado_Ruta_1 : in std_logic;
			SEM_rojo_Ruta_1 : out std_logic;
			SEM_naranja_Ruta_1 : out std_logic;
			SEM_doble_naranja_Ruta_1 : out std_logic;
			SEM_verde_Ruta_1 : out std_logic
		);
	end component sem_fsm_1;
	--componente_2 de sem_fsm
	component sem_fsm_2 is
		generic(
			N_RUT : natural := 3;
			N_SEM : natural := 3
		);
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			SEM_estado_Ruta_2 : in std_logic;
			SEM_rojo_Ruta_2 : out std_logic;
			SEM_naranja_Ruta_2 : out std_logic;
			SEM_doble_naranja_Ruta_2 : out std_logic;
			SEM_verde_Ruta_2 : out std_logic
		);
	end component sem_fsm_2;
	--componente_3 de sem_fsm
	component sem_fsm_3 is
		generic(
			N_RUT : natural := 3;
			N_SEM : natural := 3
		);
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			SEM_estado_Ruta_3 : in std_logic;
			SEM_rojo_Ruta_3 : out std_logic;
			SEM_naranja_Ruta_3 : out std_logic;
			SEM_doble_naranja_Ruta_3 : out std_logic;
			SEM_verde_Ruta_3 : out std_logic
		);
	end component sem_fsm_3;
	--componente_1 de rut_fsm
	component rut_fsm_1 is
		generic(
			N_RUT : natural := 3;
			N_SEM : natural := 3
		);
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			CV_int_Ruta_1 : in std_logic;
			CV_paralelo_Ruta_1 : in std_logic_vector(2-1 downto 0);
			CV_paralelo_temp_Ruta_1 : in std_logic_vector(3-1 downto 0);
			CV_despeje_Ruta_1 : in std_logic_vector(4-1 downto 0);
			CV_aprox_Ruta_1 : in std_logic_vector(5-1 downto 0);
			Estado_sub_ruta_Ruta_1 : in std_logic_vector(6-1 downto 0);
			Estado_ruta_cond_Ruta_1 : in std_logic_vector(7-1 downto 0);
			Estado_ruta_confl_Ruta_1 : in std_logic_vector(8-1 downto 0);
			Estado_SEM_sgte_Ruta_1 : in std_logic_vector(9-1 downto 0);
			Pos_MDC_ruta_Ruta_1 : in std_logic_vector(10-1 downto 0);
			Pos_MDC_aprox_Ruta_1 : in std_logic_vector(11-1 downto 0);
			Pos_MDC_despeje_Ruta_1 : in std_logic_vector(12-1 downto 0);
			Pos_MDC_solape_Ruta_1 : in std_logic_vector(13-1 downto 0);
			Bloq_MDC_ruta_Ruta_1 : in std_logic_vector(14-1 downto 0);
			Bloq_MDC_solape_Ruta_1 : in std_logic_vector(15-1 downto 0);
			Estado_PAN_Ruta_1 : in std_logic_vector(16-1 downto 0);
			SEM_estado_Ruta_1 : out std_logic;
			RUT_estado_Ruta_1 : out std_logic;
			RUT_sem_bloq_slp_Ruta_1 : out std_logic
		);
	end component rut_fsm_1;
	--componente_2 de rut_fsm
	component rut_fsm_2 is
		generic(
			N_RUT : natural := 3;
			N_SEM : natural := 3
		);
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			CV_int_Ruta_2 : in std_logic;
			CV_paralelo_Ruta_2 : in std_logic_vector(2-1 downto 0);
			CV_paralelo_temp_Ruta_2 : in std_logic_vector(3-1 downto 0);
			CV_despeje_Ruta_2 : in std_logic_vector(4-1 downto 0);
			CV_aprox_Ruta_2 : in std_logic_vector(5-1 downto 0);
			Estado_sub_ruta_Ruta_2 : in std_logic_vector(6-1 downto 0);
			Estado_ruta_cond_Ruta_2 : in std_logic_vector(7-1 downto 0);
			Estado_ruta_confl_Ruta_2 : in std_logic_vector(8-1 downto 0);
			Estado_SEM_sgte_Ruta_2 : in std_logic_vector(9-1 downto 0);
			Pos_MDC_ruta_Ruta_2 : in std_logic_vector(10-1 downto 0);
			Pos_MDC_aprox_Ruta_2 : in std_logic_vector(11-1 downto 0);
			Pos_MDC_despeje_Ruta_2 : in std_logic_vector(12-1 downto 0);
			Pos_MDC_solape_Ruta_2 : in std_logic_vector(13-1 downto 0);
			Bloq_MDC_ruta_Ruta_2 : in std_logic_vector(14-1 downto 0);
			Bloq_MDC_solape_Ruta_2 : in std_logic_vector(15-1 downto 0);
			Estado_PAN_Ruta_2 : in std_logic_vector(16-1 downto 0);
			SEM_estado_Ruta_2 : out std_logic;
			RUT_estado_Ruta_2 : out std_logic;
			RUT_sem_bloq_slp_Ruta_2 : out std_logic
		);
	end component rut_fsm_2;
	--componente_3 de rut_fsm
	component rut_fsm_3 is
		generic(
			N_RUT : natural := 3;
			N_SEM : natural := 3
		);
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			CV_int_Ruta_3 : in std_logic;
			CV_paralelo_Ruta_3 : in std_logic_vector(2-1 downto 0);
			CV_paralelo_temp_Ruta_3 : in std_logic_vector(3-1 downto 0);
			CV_despeje_Ruta_3 : in std_logic_vector(4-1 downto 0);
			CV_aprox_Ruta_3 : in std_logic_vector(5-1 downto 0);
			Estado_sub_ruta_Ruta_3 : in std_logic_vector(6-1 downto 0);
			Estado_ruta_cond_Ruta_3 : in std_logic_vector(7-1 downto 0);
			Estado_ruta_confl_Ruta_3 : in std_logic_vector(8-1 downto 0);
			Estado_SEM_sgte_Ruta_3 : in std_logic_vector(9-1 downto 0);
			Pos_MDC_ruta_Ruta_3 : in std_logic_vector(10-1 downto 0);
			Pos_MDC_aprox_Ruta_3 : in std_logic_vector(11-1 downto 0);
			Pos_MDC_despeje_Ruta_3 : in std_logic_vector(12-1 downto 0);
			Pos_MDC_solape_Ruta_3 : in std_logic_vector(13-1 downto 0);
			Bloq_MDC_ruta_Ruta_3 : in std_logic_vector(14-1 downto 0);
			Bloq_MDC_solape_Ruta_3 : in std_logic_vector(15-1 downto 0);
			Estado_PAN_Ruta_3 : in std_logic_vector(16-1 downto 0);
			SEM_estado_Ruta_3 : out std_logic;
			RUT_estado_Ruta_3 : out std_logic;
			RUT_sem_bloq_slp_Ruta_3 : out std_logic
		);
	end component rut_fsm_3;
	Signal cv_s,Posicion_in_s,Ruta_s,Permisos_s: std_logic_vector(N_RUT-1 downto 0);
	Signal aux_s,Rojo_in_s,Amarillo_in_s,Verde_in_s,Rojo_out_s,Amarillo_out_s,Verde_out_s,Rojo_s,Amarillo_s,Verde_s: std_logic_vector(N_SEM-1 downto 0);
	Signal aux1_s,aux2_s,Alto_s,Bajo_s,Alto_out_s,Bajo_out_s,Alto_in_s,Bajo_in_s: std_logic_vector(N_PAN-1 downto 0);
	Signal Maquina_normal_in_s,Maquina_reversa_in_s,Maquina_normal_out_s,Maquina_reversa_out_s,Maquina_normal_s,Maquina_reversa_s: std_logic_vector(N_MDC-1 downto 0);
	Signal Estado_CV_bloq_Ruta_1_s : std_logic;
	Signal Estado_ruta_bloq_Ruta_1_s : std_logic_vector(18-1 downto 0);
	Signal MDC_bloq_temp_solape_Ruta_1_s : std_logic_vector(19-1 downto 0);
	Signal Estado_CV_bloq_Ruta_2_s : std_logic;
	Signal Estado_ruta_bloq_Ruta_2_s : std_logic_vector(18-1 downto 0);
	Signal MDC_bloq_temp_solape_Ruta_2_s : std_logic_vector(19-1 downto 0);
	Signal Estado_CV_bloq_Ruta_3_s : std_logic;
	Signal Estado_ruta_bloq_Ruta_3_s : std_logic_vector(18-1 downto 0);
	Signal MDC_bloq_temp_solape_Ruta_3_s : std_logic_vector(19-1 downto 0);
	Signal MDC_normal_Ruta_1_s : std_logic;
	Signal MDC_reverso_Ruta_1_s : std_logic;
	Signal MDC_libre_Ruta_1_s : std_logic;
	Signal MDC_cerrojado_Ruta_1_s : std_logic;
	Signal MDC_normal_Ruta_2_s : std_logic;
	Signal MDC_reverso_Ruta_2_s : std_logic;
	Signal MDC_libre_Ruta_2_s : std_logic;
	Signal MDC_cerrojado_Ruta_2_s : std_logic;
	Signal MDC_normal_Ruta_3_s : std_logic;
	Signal MDC_reverso_Ruta_3_s : std_logic;
	Signal MDC_libre_Ruta_3_s : std_logic;
	Signal MDC_cerrojado_Ruta_3_s : std_logic;
	Signal Estado_ruta_Ruta_1_s : std_logic_vector(20-1 downto 0);
	Signal CV_alarma_total_Ruta_1_s : std_logic_vector(21-1 downto 0);
	Signal CV_alarma_inmediata_Ruta_1_s : std_logic_vector(22-1 downto 0);
	Signal PAN_bloq_temp_solape_Ruta_1_s : std_logic_vector(23-1 downto 0);
	Signal Estado_ruta_Ruta_2_s : std_logic_vector(20-1 downto 0);
	Signal CV_alarma_total_Ruta_2_s : std_logic_vector(21-1 downto 0);
	Signal CV_alarma_inmediata_Ruta_2_s : std_logic_vector(22-1 downto 0);
	Signal PAN_bloq_temp_solape_Ruta_2_s : std_logic_vector(23-1 downto 0);
	Signal Estado_ruta_Ruta_3_s : std_logic_vector(20-1 downto 0);
	Signal CV_alarma_total_Ruta_3_s : std_logic_vector(21-1 downto 0);
	Signal CV_alarma_inmediata_Ruta_3_s : std_logic_vector(22-1 downto 0);
	Signal PAN_bloq_temp_solape_Ruta_3_s : std_logic_vector(23-1 downto 0);
	Signal PAN_alto_Ruta_1_s : std_logic;
	Signal PAN_bajo_Ruta_1_s : std_logic;
	Signal PAN_alarma_Ruta_1_s : std_logic;
	Signal PAN_habilitacion_Ruta_1_s : std_logic;
	Signal PAN_alto_Ruta_2_s : std_logic;
	Signal PAN_bajo_Ruta_2_s : std_logic;
	Signal PAN_alarma_Ruta_2_s : std_logic;
	Signal PAN_habilitacion_Ruta_2_s : std_logic;
	Signal PAN_alto_Ruta_3_s : std_logic;
	Signal PAN_bajo_Ruta_3_s : std_logic;
	Signal PAN_alarma_Ruta_3_s : std_logic;
	Signal PAN_habilitacion_Ruta_3_s : std_logic;
	Signal SEM_rojo_Ruta_1_s : std_logic;
	Signal SEM_naranja_Ruta_1_s : std_logic;
	Signal SEM_doble_naranja_Ruta_1_s : std_logic;
	Signal SEM_verde_Ruta_1_s : std_logic;
	Signal SEM_rojo_Ruta_2_s : std_logic;
	Signal SEM_naranja_Ruta_2_s : std_logic;
	Signal SEM_doble_naranja_Ruta_2_s : std_logic;
	Signal SEM_verde_Ruta_2_s : std_logic;
	Signal SEM_rojo_Ruta_3_s : std_logic;
	Signal SEM_naranja_Ruta_3_s : std_logic;
	Signal SEM_doble_naranja_Ruta_3_s : std_logic;
	Signal SEM_verde_Ruta_3_s : std_logic;
	Signal CV_int_Ruta_1_s : std_logic;
	Signal CV_paralelo_Ruta_1_s : std_logic_vector(2-1 downto 0);
	Signal CV_paralelo_temp_Ruta_1_s : std_logic_vector(3-1 downto 0);
	Signal CV_despeje_Ruta_1_s : std_logic_vector(4-1 downto 0);
	Signal CV_aprox_Ruta_1_s : std_logic_vector(5-1 downto 0);
	Signal Estado_sub_ruta_Ruta_1_s : std_logic_vector(6-1 downto 0);
	Signal Estado_ruta_cond_Ruta_1_s : std_logic_vector(7-1 downto 0);
	Signal Estado_ruta_confl_Ruta_1_s : std_logic_vector(8-1 downto 0);
	Signal Estado_SEM_sgte_Ruta_1_s : std_logic_vector(9-1 downto 0);
	Signal Pos_MDC_ruta_Ruta_1_s : std_logic_vector(10-1 downto 0);
	Signal Pos_MDC_aprox_Ruta_1_s : std_logic_vector(11-1 downto 0);
	Signal Pos_MDC_despeje_Ruta_1_s : std_logic_vector(12-1 downto 0);
	Signal Pos_MDC_solape_Ruta_1_s : std_logic_vector(13-1 downto 0);
	Signal Bloq_MDC_ruta_Ruta_1_s : std_logic_vector(14-1 downto 0);
	Signal Bloq_MDC_solape_Ruta_1_s : std_logic_vector(15-1 downto 0);
	Signal Estado_PAN_Ruta_1_s : std_logic_vector(16-1 downto 0);
	Signal CV_int_Ruta_2_s : std_logic;
	Signal CV_paralelo_Ruta_2_s : std_logic_vector(2-1 downto 0);
	Signal CV_paralelo_temp_Ruta_2_s : std_logic_vector(3-1 downto 0);
	Signal CV_despeje_Ruta_2_s : std_logic_vector(4-1 downto 0);
	Signal CV_aprox_Ruta_2_s : std_logic_vector(5-1 downto 0);
	Signal Estado_sub_ruta_Ruta_2_s : std_logic_vector(6-1 downto 0);
	Signal Estado_ruta_cond_Ruta_2_s : std_logic_vector(7-1 downto 0);
	Signal Estado_ruta_confl_Ruta_2_s : std_logic_vector(8-1 downto 0);
	Signal Estado_SEM_sgte_Ruta_2_s : std_logic_vector(9-1 downto 0);
	Signal Pos_MDC_ruta_Ruta_2_s : std_logic_vector(10-1 downto 0);
	Signal Pos_MDC_aprox_Ruta_2_s : std_logic_vector(11-1 downto 0);
	Signal Pos_MDC_despeje_Ruta_2_s : std_logic_vector(12-1 downto 0);
	Signal Pos_MDC_solape_Ruta_2_s : std_logic_vector(13-1 downto 0);
	Signal Bloq_MDC_ruta_Ruta_2_s : std_logic_vector(14-1 downto 0);
	Signal Bloq_MDC_solape_Ruta_2_s : std_logic_vector(15-1 downto 0);
	Signal Estado_PAN_Ruta_2_s : std_logic_vector(16-1 downto 0);
	Signal CV_int_Ruta_3_s : std_logic;
	Signal CV_paralelo_Ruta_3_s : std_logic_vector(2-1 downto 0);
	Signal CV_paralelo_temp_Ruta_3_s : std_logic_vector(3-1 downto 0);
	Signal CV_despeje_Ruta_3_s : std_logic_vector(4-1 downto 0);
	Signal CV_aprox_Ruta_3_s : std_logic_vector(5-1 downto 0);
	Signal Estado_sub_ruta_Ruta_3_s : std_logic_vector(6-1 downto 0);
	Signal Estado_ruta_cond_Ruta_3_s : std_logic_vector(7-1 downto 0);
	Signal Estado_ruta_confl_Ruta_3_s : std_logic_vector(8-1 downto 0);
	Signal Estado_SEM_sgte_Ruta_3_s : std_logic_vector(9-1 downto 0);
	Signal Pos_MDC_ruta_Ruta_3_s : std_logic_vector(10-1 downto 0);
	Signal Pos_MDC_aprox_Ruta_3_s : std_logic_vector(11-1 downto 0);
	Signal Pos_MDC_despeje_Ruta_3_s : std_logic_vector(12-1 downto 0);
	Signal Pos_MDC_solape_Ruta_3_s : std_logic_vector(13-1 downto 0);
	Signal Bloq_MDC_ruta_Ruta_3_s : std_logic_vector(14-1 downto 0);
	Signal Bloq_MDC_solape_Ruta_3_s : std_logic_vector(15-1 downto 0);
	Signal Estado_PAN_Ruta_3_s : std_logic_vector(16-1 downto 0);
	Signal SEM_estado_Ruta_1_s : std_logic;
	Signal RUT_estado_Ruta_1_s : std_logic;
	Signal RUT_sem_bloq_slp_Ruta_1_s : std_logic;
	Signal SEM_estado_Ruta_2_s : std_logic;
	Signal RUT_estado_Ruta_2_s : std_logic;
	Signal RUT_sem_bloq_slp_Ruta_2_s : std_logic;
	Signal SEM_estado_Ruta_3_s : std_logic;
	Signal RUT_estado_Ruta_3_s : std_logic;
	Signal RUT_sem_bloq_slp_Ruta_3_s : std_logic;
	Signal Reset_sem_s,Reset_Pan_s: std_logic;
	begin
	mdc_fsm_inst_1:mdc_fsm_1 port map(
		Clock => Clock,
		Estado_CV_bloq_Ruta_1 => Estado_CV_bloq_Ruta_1_s,
		Estado_ruta_bloq_Ruta_1 => Estado_ruta_bloq_Ruta_1_s,
		MDC_bloq_temp_solape_Ruta_1 => MDC_bloq_temp_solape_Ruta_1_s,
		MDC_normal_Ruta_1 => MDC_normal_Ruta_1_s,
		MDC_reverso_Ruta_1 => MDC_reverso_Ruta_1_s,
		MDC_libre_Ruta_1 => MDC_libre_Ruta_1_s,
		MDC_cerrojado_Ruta_1 => MDC_cerrojado_Ruta_1_s,
		Reset => Reset);
	mdc_fsm_inst_2:mdc_fsm_2 port map(
		Clock => Clock,
		Estado_CV_bloq_Ruta_2 => Estado_CV_bloq_Ruta_2_s,
		Estado_ruta_bloq_Ruta_2 => Estado_ruta_bloq_Ruta_2_s,
		MDC_bloq_temp_solape_Ruta_2 => MDC_bloq_temp_solape_Ruta_2_s,
		MDC_normal_Ruta_2 => MDC_normal_Ruta_2_s,
		MDC_reverso_Ruta_2 => MDC_reverso_Ruta_2_s,
		MDC_libre_Ruta_2 => MDC_libre_Ruta_2_s,
		MDC_cerrojado_Ruta_2 => MDC_cerrojado_Ruta_2_s,
		Reset => Reset);
	mdc_fsm_inst_3:mdc_fsm_3 port map(
		Clock => Clock,
		Estado_CV_bloq_Ruta_3 => Estado_CV_bloq_Ruta_3_s,
		Estado_ruta_bloq_Ruta_3 => Estado_ruta_bloq_Ruta_3_s,
		MDC_bloq_temp_solape_Ruta_3 => MDC_bloq_temp_solape_Ruta_3_s,
		MDC_normal_Ruta_3 => MDC_normal_Ruta_3_s,
		MDC_reverso_Ruta_3 => MDC_reverso_Ruta_3_s,
		MDC_libre_Ruta_3 => MDC_libre_Ruta_3_s,
		MDC_cerrojado_Ruta_3 => MDC_cerrojado_Ruta_3_s,
		Reset => Reset);
	pan_fsm_inst_1:pan_fsm_1 port map(
		Clock => Clock,
		Estado_ruta_Ruta_1 => Estado_ruta_Ruta_1_s,
		CV_alarma_total_Ruta_1 => CV_alarma_total_Ruta_1_s,
		CV_alarma_inmediata_Ruta_1 => CV_alarma_inmediata_Ruta_1_s,
		PAN_bloq_temp_solape_Ruta_1 => PAN_bloq_temp_solape_Ruta_1_s,
		PAN_alto_Ruta_1 => PAN_alto_Ruta_1_s,
		PAN_bajo_Ruta_1 => PAN_bajo_Ruta_1_s,
		PAN_alarma_Ruta_1 => PAN_alarma_Ruta_1_s,
		PAN_habilitacion_Ruta_1 => PAN_habilitacion_Ruta_1_s,
		Reset => Reset);
	pan_fsm_inst_2:pan_fsm_2 port map(
		Clock => Clock,
		Estado_ruta_Ruta_2 => Estado_ruta_Ruta_2_s,
		CV_alarma_total_Ruta_2 => CV_alarma_total_Ruta_2_s,
		CV_alarma_inmediata_Ruta_2 => CV_alarma_inmediata_Ruta_2_s,
		PAN_bloq_temp_solape_Ruta_2 => PAN_bloq_temp_solape_Ruta_2_s,
		PAN_alto_Ruta_2 => PAN_alto_Ruta_2_s,
		PAN_bajo_Ruta_2 => PAN_bajo_Ruta_2_s,
		PAN_alarma_Ruta_2 => PAN_alarma_Ruta_2_s,
		PAN_habilitacion_Ruta_2 => PAN_habilitacion_Ruta_2_s,
		Reset => Reset);
	pan_fsm_inst_3:pan_fsm_3 port map(
		Clock => Clock,
		Estado_ruta_Ruta_3 => Estado_ruta_Ruta_3_s,
		CV_alarma_total_Ruta_3 => CV_alarma_total_Ruta_3_s,
		CV_alarma_inmediata_Ruta_3 => CV_alarma_inmediata_Ruta_3_s,
		PAN_bloq_temp_solape_Ruta_3 => PAN_bloq_temp_solape_Ruta_3_s,
		PAN_alto_Ruta_3 => PAN_alto_Ruta_3_s,
		PAN_bajo_Ruta_3 => PAN_bajo_Ruta_3_s,
		PAN_alarma_Ruta_3 => PAN_alarma_Ruta_3_s,
		PAN_habilitacion_Ruta_3 => PAN_habilitacion_Ruta_3_s,
		Reset => Reset);
	sem_fsm_inst_1:sem_fsm_1 port map(
		Clock => Clock,
		SEM_estado_Ruta_1 => SEM_estado_Ruta_1_s,
		SEM_rojo_Ruta_1 => SEM_rojo_Ruta_1_s,
		SEM_naranja_Ruta_1 => SEM_naranja_Ruta_1_s,
		SEM_doble_naranja_Ruta_1 => SEM_doble_naranja_Ruta_1_s,
		SEM_verde_Ruta_1 => SEM_verde_Ruta_1_s,
		Reset => Reset);
	sem_fsm_inst_2:sem_fsm_2 port map(
		Clock => Clock,
		SEM_estado_Ruta_2 => SEM_estado_Ruta_2_s,
		SEM_rojo_Ruta_2 => SEM_rojo_Ruta_2_s,
		SEM_naranja_Ruta_2 => SEM_naranja_Ruta_2_s,
		SEM_doble_naranja_Ruta_2 => SEM_doble_naranja_Ruta_2_s,
		SEM_verde_Ruta_2 => SEM_verde_Ruta_2_s,
		Reset => Reset);
	sem_fsm_inst_3:sem_fsm_3 port map(
		Clock => Clock,
		SEM_estado_Ruta_3 => SEM_estado_Ruta_3_s,
		SEM_rojo_Ruta_3 => SEM_rojo_Ruta_3_s,
		SEM_naranja_Ruta_3 => SEM_naranja_Ruta_3_s,
		SEM_doble_naranja_Ruta_3 => SEM_doble_naranja_Ruta_3_s,
		SEM_verde_Ruta_3 => SEM_verde_Ruta_3_s,
		Reset => Reset);
	rut_fsm_inst_1:rut_fsm_1 port map(
		Clock => Clock,
		CV_int_Ruta_1 => CV_int_Ruta_1_s,
		CV_paralelo_Ruta_1 => CV_paralelo_Ruta_1_s,
		CV_paralelo_temp_Ruta_1 => CV_paralelo_temp_Ruta_1_s,
		CV_despeje_Ruta_1 => CV_despeje_Ruta_1_s,
		CV_aprox_Ruta_1 => CV_aprox_Ruta_1_s,
		Estado_sub_ruta_Ruta_1 => Estado_sub_ruta_Ruta_1_s,
		Estado_ruta_cond_Ruta_1 => Estado_ruta_cond_Ruta_1_s,
		Estado_ruta_confl_Ruta_1 => Estado_ruta_confl_Ruta_1_s,
		Estado_SEM_sgte_Ruta_1 => Estado_SEM_sgte_Ruta_1_s,
		Pos_MDC_ruta_Ruta_1 => Pos_MDC_ruta_Ruta_1_s,
		Pos_MDC_aprox_Ruta_1 => Pos_MDC_aprox_Ruta_1_s,
		Pos_MDC_despeje_Ruta_1 => Pos_MDC_despeje_Ruta_1_s,
		Pos_MDC_solape_Ruta_1 => Pos_MDC_solape_Ruta_1_s,
		Bloq_MDC_ruta_Ruta_1 => Bloq_MDC_ruta_Ruta_1_s,
		Bloq_MDC_solape_Ruta_1 => Bloq_MDC_solape_Ruta_1_s,
		Estado_PAN_Ruta_1 => Estado_PAN_Ruta_1_s,
		SEM_estado_Ruta_1 => SEM_estado_Ruta_1_s,
		RUT_estado_Ruta_1 => RUT_estado_Ruta_1_s,
		RUT_sem_bloq_slp_Ruta_1 => RUT_sem_bloq_slp_Ruta_1_s,
		Reset => Reset);
	rut_fsm_inst_2:rut_fsm_2 port map(
		Clock => Clock,
		CV_int_Ruta_2 => CV_int_Ruta_2_s,
		CV_paralelo_Ruta_2 => CV_paralelo_Ruta_2_s,
		CV_paralelo_temp_Ruta_2 => CV_paralelo_temp_Ruta_2_s,
		CV_despeje_Ruta_2 => CV_despeje_Ruta_2_s,
		CV_aprox_Ruta_2 => CV_aprox_Ruta_2_s,
		Estado_sub_ruta_Ruta_2 => Estado_sub_ruta_Ruta_2_s,
		Estado_ruta_cond_Ruta_2 => Estado_ruta_cond_Ruta_2_s,
		Estado_ruta_confl_Ruta_2 => Estado_ruta_confl_Ruta_2_s,
		Estado_SEM_sgte_Ruta_2 => Estado_SEM_sgte_Ruta_2_s,
		Pos_MDC_ruta_Ruta_2 => Pos_MDC_ruta_Ruta_2_s,
		Pos_MDC_aprox_Ruta_2 => Pos_MDC_aprox_Ruta_2_s,
		Pos_MDC_despeje_Ruta_2 => Pos_MDC_despeje_Ruta_2_s,
		Pos_MDC_solape_Ruta_2 => Pos_MDC_solape_Ruta_2_s,
		Bloq_MDC_ruta_Ruta_2 => Bloq_MDC_ruta_Ruta_2_s,
		Bloq_MDC_solape_Ruta_2 => Bloq_MDC_solape_Ruta_2_s,
		Estado_PAN_Ruta_2 => Estado_PAN_Ruta_2_s,
		SEM_estado_Ruta_2 => SEM_estado_Ruta_2_s,
		RUT_estado_Ruta_2 => RUT_estado_Ruta_2_s,
		RUT_sem_bloq_slp_Ruta_2 => RUT_sem_bloq_slp_Ruta_2_s,
		Reset => Reset);
	rut_fsm_inst_3:rut_fsm_3 port map(
		Clock => Clock,
		CV_int_Ruta_3 => CV_int_Ruta_3_s,
		CV_paralelo_Ruta_3 => CV_paralelo_Ruta_3_s,
		CV_paralelo_temp_Ruta_3 => CV_paralelo_temp_Ruta_3_s,
		CV_despeje_Ruta_3 => CV_despeje_Ruta_3_s,
		CV_aprox_Ruta_3 => CV_aprox_Ruta_3_s,
		Estado_sub_ruta_Ruta_3 => Estado_sub_ruta_Ruta_3_s,
		Estado_ruta_cond_Ruta_3 => Estado_ruta_cond_Ruta_3_s,
		Estado_ruta_confl_Ruta_3 => Estado_ruta_confl_Ruta_3_s,
		Estado_SEM_sgte_Ruta_3 => Estado_SEM_sgte_Ruta_3_s,
		Pos_MDC_ruta_Ruta_3 => Pos_MDC_ruta_Ruta_3_s,
		Pos_MDC_aprox_Ruta_3 => Pos_MDC_aprox_Ruta_3_s,
		Pos_MDC_despeje_Ruta_3 => Pos_MDC_despeje_Ruta_3_s,
		Pos_MDC_solape_Ruta_3 => Pos_MDC_solape_Ruta_3_s,
		Bloq_MDC_ruta_Ruta_3 => Bloq_MDC_ruta_Ruta_3_s,
		Bloq_MDC_solape_Ruta_3 => Bloq_MDC_solape_Ruta_3_s,
		Estado_PAN_Ruta_3 => Estado_PAN_Ruta_3_s,
		SEM_estado_Ruta_3 => SEM_estado_Ruta_3_s,
		RUT_estado_Ruta_3 => RUT_estado_Ruta_3_s,
		RUT_sem_bloq_slp_Ruta_3 => RUT_sem_bloq_slp_Ruta_3_s,
		Reset => Reset);
	Estado_CV_bloq_Ruta_1_s <= Estado_CV_bloq_Ruta_1;
	Estado_ruta_bloq_Ruta_1_s <= Estado_ruta_bloq_Ruta_1;
	MDC_bloq_temp_solape_Ruta_1_s <= MDC_bloq_temp_solape_Ruta_1;

	Estado_CV_bloq_Ruta_2_s <= Estado_CV_bloq_Ruta_2;
	Estado_ruta_bloq_Ruta_2_s <= Estado_ruta_bloq_Ruta_2;
	MDC_bloq_temp_solape_Ruta_2_s <= MDC_bloq_temp_solape_Ruta_2;

	Estado_CV_bloq_Ruta_3_s <= Estado_CV_bloq_Ruta_3;
	Estado_ruta_bloq_Ruta_3_s <= Estado_ruta_bloq_Ruta_3;
	MDC_bloq_temp_solape_Ruta_3_s <= MDC_bloq_temp_solape_Ruta_3;

	MDC_normal_Ruta_1 <= MDC_normal_Ruta_1_s;
	MDC_reverso_Ruta_1 <= MDC_reverso_Ruta_1_s;
	MDC_libre_Ruta_1 <= MDC_libre_Ruta_1_s;
	MDC_cerrojado_Ruta_1 <= MDC_cerrojado_Ruta_1_s;

	MDC_normal_Ruta_2 <= MDC_normal_Ruta_2_s;
	MDC_reverso_Ruta_2 <= MDC_reverso_Ruta_2_s;
	MDC_libre_Ruta_2 <= MDC_libre_Ruta_2_s;
	MDC_cerrojado_Ruta_2 <= MDC_cerrojado_Ruta_2_s;

	MDC_normal_Ruta_3 <= MDC_normal_Ruta_3_s;
	MDC_reverso_Ruta_3 <= MDC_reverso_Ruta_3_s;
	MDC_libre_Ruta_3 <= MDC_libre_Ruta_3_s;
	MDC_cerrojado_Ruta_3 <= MDC_cerrojado_Ruta_3_s;

	Estado_ruta_Ruta_1_s <= Estado_ruta_Ruta_1;
	CV_alarma_total_Ruta_1_s <= CV_alarma_total_Ruta_1;
	CV_alarma_inmediata_Ruta_1_s <= CV_alarma_inmediata_Ruta_1;
	PAN_bloq_temp_solape_Ruta_1_s <= PAN_bloq_temp_solape_Ruta_1;

	Estado_ruta_Ruta_2_s <= Estado_ruta_Ruta_2;
	CV_alarma_total_Ruta_2_s <= CV_alarma_total_Ruta_2;
	CV_alarma_inmediata_Ruta_2_s <= CV_alarma_inmediata_Ruta_2;
	PAN_bloq_temp_solape_Ruta_2_s <= PAN_bloq_temp_solape_Ruta_2;

	Estado_ruta_Ruta_3_s <= Estado_ruta_Ruta_3;
	CV_alarma_total_Ruta_3_s <= CV_alarma_total_Ruta_3;
	CV_alarma_inmediata_Ruta_3_s <= CV_alarma_inmediata_Ruta_3;
	PAN_bloq_temp_solape_Ruta_3_s <= PAN_bloq_temp_solape_Ruta_3;

	PAN_alto_Ruta_1 <= PAN_alto_Ruta_1_s;
	PAN_bajo_Ruta_1 <= PAN_bajo_Ruta_1_s;
	PAN_alarma_Ruta_1 <= PAN_alarma_Ruta_1_s;
	PAN_habilitacion_Ruta_1 <= PAN_habilitacion_Ruta_1_s;

	PAN_alto_Ruta_2 <= PAN_alto_Ruta_2_s;
	PAN_bajo_Ruta_2 <= PAN_bajo_Ruta_2_s;
	PAN_alarma_Ruta_2 <= PAN_alarma_Ruta_2_s;
	PAN_habilitacion_Ruta_2 <= PAN_habilitacion_Ruta_2_s;

	PAN_alto_Ruta_3 <= PAN_alto_Ruta_3_s;
	PAN_bajo_Ruta_3 <= PAN_bajo_Ruta_3_s;
	PAN_alarma_Ruta_3 <= PAN_alarma_Ruta_3_s;
	PAN_habilitacion_Ruta_3 <= PAN_habilitacion_Ruta_3_s;

	SEM_rojo_Ruta_1 <= SEM_rojo_Ruta_1_s;
	SEM_naranja_Ruta_1 <= SEM_naranja_Ruta_1_s;
	SEM_doble_naranja_Ruta_1 <= SEM_doble_naranja_Ruta_1_s;
	SEM_verde_Ruta_1 <= SEM_verde_Ruta_1_s;

	SEM_rojo_Ruta_2 <= SEM_rojo_Ruta_2_s;
	SEM_naranja_Ruta_2 <= SEM_naranja_Ruta_2_s;
	SEM_doble_naranja_Ruta_2 <= SEM_doble_naranja_Ruta_2_s;
	SEM_verde_Ruta_2 <= SEM_verde_Ruta_2_s;

	SEM_rojo_Ruta_3 <= SEM_rojo_Ruta_3_s;
	SEM_naranja_Ruta_3 <= SEM_naranja_Ruta_3_s;
	SEM_doble_naranja_Ruta_3 <= SEM_doble_naranja_Ruta_3_s;
	SEM_verde_Ruta_3 <= SEM_verde_Ruta_3_s;

	CV_int_Ruta_1_s <= CV_int_Ruta_1;
	CV_paralelo_Ruta_1_s <= CV_paralelo_Ruta_1;
	CV_paralelo_temp_Ruta_1_s <= CV_paralelo_temp_Ruta_1;
	CV_despeje_Ruta_1_s <= CV_despeje_Ruta_1;
	CV_aprox_Ruta_1_s <= CV_aprox_Ruta_1;
	Estado_sub_ruta_Ruta_1_s <= Estado_sub_ruta_Ruta_1;
	Estado_ruta_cond_Ruta_1_s <= Estado_ruta_cond_Ruta_1;
	Estado_ruta_confl_Ruta_1_s <= Estado_ruta_confl_Ruta_1;
	Estado_SEM_sgte_Ruta_1_s <= Estado_SEM_sgte_Ruta_1;
	Pos_MDC_ruta_Ruta_1_s <= Pos_MDC_ruta_Ruta_1;
	Pos_MDC_aprox_Ruta_1_s <= Pos_MDC_aprox_Ruta_1;
	Pos_MDC_despeje_Ruta_1_s <= Pos_MDC_despeje_Ruta_1;
	Pos_MDC_solape_Ruta_1_s <= Pos_MDC_solape_Ruta_1;
	Bloq_MDC_ruta_Ruta_1_s <= Bloq_MDC_ruta_Ruta_1;
	Bloq_MDC_solape_Ruta_1_s <= Bloq_MDC_solape_Ruta_1;
	Estado_PAN_Ruta_1_s <= Estado_PAN_Ruta_1;

	CV_int_Ruta_2_s <= CV_int_Ruta_2;
	CV_paralelo_Ruta_2_s <= CV_paralelo_Ruta_2;
	CV_paralelo_temp_Ruta_2_s <= CV_paralelo_temp_Ruta_2;
	CV_despeje_Ruta_2_s <= CV_despeje_Ruta_2;
	CV_aprox_Ruta_2_s <= CV_aprox_Ruta_2;
	Estado_sub_ruta_Ruta_2_s <= Estado_sub_ruta_Ruta_2;
	Estado_ruta_cond_Ruta_2_s <= Estado_ruta_cond_Ruta_2;
	Estado_ruta_confl_Ruta_2_s <= Estado_ruta_confl_Ruta_2;
	Estado_SEM_sgte_Ruta_2_s <= Estado_SEM_sgte_Ruta_2;
	Pos_MDC_ruta_Ruta_2_s <= Pos_MDC_ruta_Ruta_2;
	Pos_MDC_aprox_Ruta_2_s <= Pos_MDC_aprox_Ruta_2;
	Pos_MDC_despeje_Ruta_2_s <= Pos_MDC_despeje_Ruta_2;
	Pos_MDC_solape_Ruta_2_s <= Pos_MDC_solape_Ruta_2;
	Bloq_MDC_ruta_Ruta_2_s <= Bloq_MDC_ruta_Ruta_2;
	Bloq_MDC_solape_Ruta_2_s <= Bloq_MDC_solape_Ruta_2;
	Estado_PAN_Ruta_2_s <= Estado_PAN_Ruta_2;

	CV_int_Ruta_3_s <= CV_int_Ruta_3;
	CV_paralelo_Ruta_3_s <= CV_paralelo_Ruta_3;
	CV_paralelo_temp_Ruta_3_s <= CV_paralelo_temp_Ruta_3;
	CV_despeje_Ruta_3_s <= CV_despeje_Ruta_3;
	CV_aprox_Ruta_3_s <= CV_aprox_Ruta_3;
	Estado_sub_ruta_Ruta_3_s <= Estado_sub_ruta_Ruta_3;
	Estado_ruta_cond_Ruta_3_s <= Estado_ruta_cond_Ruta_3;
	Estado_ruta_confl_Ruta_3_s <= Estado_ruta_confl_Ruta_3;
	Estado_SEM_sgte_Ruta_3_s <= Estado_SEM_sgte_Ruta_3;
	Pos_MDC_ruta_Ruta_3_s <= Pos_MDC_ruta_Ruta_3;
	Pos_MDC_aprox_Ruta_3_s <= Pos_MDC_aprox_Ruta_3;
	Pos_MDC_despeje_Ruta_3_s <= Pos_MDC_despeje_Ruta_3;
	Pos_MDC_solape_Ruta_3_s <= Pos_MDC_solape_Ruta_3;
	Bloq_MDC_ruta_Ruta_3_s <= Bloq_MDC_ruta_Ruta_3;
	Bloq_MDC_solape_Ruta_3_s <= Bloq_MDC_solape_Ruta_3;
	Estado_PAN_Ruta_3_s <= Estado_PAN_Ruta_3;

	RUT_estado_Ruta_1 <= RUT_estado_Ruta_1_s;
	RUT_sem_bloq_slp_Ruta_1 <= RUT_sem_bloq_slp_Ruta_1_s;

	RUT_estado_Ruta_2 <= RUT_estado_Ruta_2_s;
	RUT_sem_bloq_slp_Ruta_2 <= RUT_sem_bloq_slp_Ruta_2_s;

	RUT_estado_Ruta_3 <= RUT_estado_Ruta_3_s;
	RUT_sem_bloq_slp_Ruta_3 <= RUT_sem_bloq_slp_Ruta_3_s;

end architecture enrutador_ARQ;
