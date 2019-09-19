-- unidad_central_enclavamiento.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad de nodo
entity nodo is
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
		Modo : in std_logic_vector(N_RUT-1 downto 0);
		Ruta_in : in std_logic_vector(N_RUT-1 downto 0);
		Semaforo_rojo_out : out std_logic_vector(N_RUT-1 downto 0)
	);
end entity nodo;
-- Arquitectura del señalamiento : Descripcion del comportamiento
architecture unidad_central_enclavamiento_ARQ of unidad_central_enclavamiento is
	--componente de nodo
	component nodo is
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
			Modo : in std_logic_vector(N_RUT-1 downto 0);
			Ruta_in : in std_logic_vector(N_RUT-1 downto 0);
			Semaforo_rojo_out : out std_logic_vector(N_RUT-1 downto 0)
		);
	end component nodo;
	Signal aux1_a,aux2_a,aux1_b,aux2_b,aux1_c,aux2_c,cv_s,Posicion_in_s,Permisos_s: std_logic_vector(N-1 downto 0);
	Signal Cosa_1_a,Cosa_2_a,Cosa_3_a,Cosa_4_a,Cosa_5_a: std_logic_vector(N-1 downto 0);
	Signal Cosa_1_b,Cosa_2_b,Cosa_3_b,Cosa_4_b,Cosa_5_b: std_logic_vector(N-1 downto 0);
	Signal Cosa_1_c,Cosa_2_c,Cosa_3_c,Cosa_4_c,Cosa_5_c: std_logic_vector(N-1 downto 0);
	Signal Ruta_in_s: std_logic_vector(N_RUT-1 downto 0);
	Signal Rojo_a,Amarillo_a,Verde_a,Rojo_b,Amarillo_b,Verde_b,Rojo_in_s,Amarillo_in_s,Verde_in_s,Rojo_out_s,Amarillo_out_s,Verde_out_s,Rojo_s,Amarillo_s,Verde_s: std_logic_vector(N_SEM-1 downto 0);
	Signal Alto_a,Bajo_a,Alto_b,Bajo_b,Alto_s,Bajo_s,Alto_out_s,Bajo_out_s,Alto_in_s,Bajo_in_s: std_logic_vector(N_PAN-1 downto 0);
	Signal Maquina_normal_a,Maquina_reversa_a,Maquina_normal_b,Maquina_reversa_b,Maquina_normal_in_s,Maquina_reversa_in_s,Maquina_normal_out_s,Maquina_reversa_out_s,Maquina_normal_s,Maquina_reversa_s: std_logic_vector(N_MDC-1 downto 0);
	Signal Reset_sem_s,Reset_Pan_s: std_logic;
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
	Signal Estado_CV_bloq_Ruta_1_s : std_logic;
	Signal Estado_ruta_bloq_Ruta_1_s : std_logic_vector(18-1 downto 0);
	Signal MDC_bloq_temp_solape_Ruta_1_s : std_logic_vector(19-1 downto 0);
	Signal Estado_ruta_Ruta_1_s : std_logic_vector(20-1 downto 0);
	Signal CV_alarma_total_Ruta_1_s : std_logic_vector(21-1 downto 0);
	Signal CV_alarma_inmediata_Ruta_1_s : std_logic_vector(22-1 downto 0);
	Signal PAN_bloq_temp_solape_Ruta_1_s : std_logic_vector(23-1 downto 0);
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
	Signal Estado_CV_bloq_Ruta_2_s : std_logic;
	Signal Estado_ruta_bloq_Ruta_2_s : std_logic_vector(18-1 downto 0);
	Signal MDC_bloq_temp_solape_Ruta_2_s : std_logic_vector(19-1 downto 0);
	Signal Estado_ruta_Ruta_2_s : std_logic_vector(20-1 downto 0);
	Signal CV_alarma_total_Ruta_2_s : std_logic_vector(21-1 downto 0);
	Signal CV_alarma_inmediata_Ruta_2_s : std_logic_vector(22-1 downto 0);
	Signal PAN_bloq_temp_solape_Ruta_2_s : std_logic_vector(23-1 downto 0);
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
	Signal Estado_CV_bloq_Ruta_3_s : std_logic;
	Signal Estado_ruta_bloq_Ruta_3_s : std_logic_vector(18-1 downto 0);
	Signal MDC_bloq_temp_solape_Ruta_3_s : std_logic_vector(19-1 downto 0);
	Signal Estado_ruta_Ruta_3_s : std_logic_vector(20-1 downto 0);
	Signal CV_alarma_total_Ruta_3_s : std_logic_vector(21-1 downto 0);
	Signal CV_alarma_inmediata_Ruta_3_s : std_logic_vector(22-1 downto 0);
	Signal PAN_bloq_temp_solape_Ruta_3_s : std_logic_vector(23-1 downto 0);
	Signal SEM_rojo_Ruta_1_s : std_logic;
	Signal SEM_naranja_Ruta_1_s : std_logic;
	Signal SEM_doble_naranja_Ruta_1_s : std_logic;
	Signal SEM_verde_Ruta_1_s : std_logic;
	Signal MDC_normal_Ruta_1_s : std_logic;
	Signal MDC_reverso_Ruta_1_s : std_logic;
	Signal MDC_libre_Ruta_1_s : std_logic;
	Signal MDC_cerrojado_Ruta_1_s : std_logic;
	Signal PAN_alto_Ruta_1_s : std_logic;
	Signal PAN_bajo_Ruta_1_s : std_logic;
	Signal PAN_alarma_Ruta_1_s : std_logic;
	Signal PAN_habilitacion_Ruta_1_s : std_logic;
	Signal RUT_estado_Ruta_1_s : std_logic;
	Signal RUT_sem_bloq_slp_Ruta_1_s : std_logic;
	Signal SEM_rojo_Ruta_2_s : std_logic;
	Signal SEM_naranja_Ruta_2_s : std_logic;
	Signal SEM_doble_naranja_Ruta_2_s : std_logic;
	Signal SEM_verde_Ruta_2_s : std_logic;
	Signal MDC_normal_Ruta_2_s : std_logic;
	Signal MDC_reverso_Ruta_2_s : std_logic;
	Signal MDC_libre_Ruta_2_s : std_logic;
	Signal MDC_cerrojado_Ruta_2_s : std_logic;
	Signal PAN_alto_Ruta_2_s : std_logic;
	Signal PAN_bajo_Ruta_2_s : std_logic;
	Signal PAN_alarma_Ruta_2_s : std_logic;
	Signal PAN_habilitacion_Ruta_2_s : std_logic;
	Signal RUT_estado_Ruta_2_s : std_logic;
	Signal RUT_sem_bloq_slp_Ruta_2_s : std_logic;
	Signal SEM_rojo_Ruta_3_s : std_logic;
	Signal SEM_naranja_Ruta_3_s : std_logic;
	Signal SEM_doble_naranja_Ruta_3_s : std_logic;
	Signal SEM_verde_Ruta_3_s : std_logic;
	Signal MDC_normal_Ruta_3_s : std_logic;
	Signal MDC_reverso_Ruta_3_s : std_logic;
	Signal MDC_libre_Ruta_3_s : std_logic;
	Signal MDC_cerrojado_Ruta_3_s : std_logic;
	Signal PAN_alto_Ruta_3_s : std_logic;
	Signal PAN_bajo_Ruta_3_s : std_logic;
	Signal PAN_alarma_Ruta_3_s : std_logic;
	Signal PAN_habilitacion_Ruta_3_s : std_logic;
	Signal RUT_estado_Ruta_3_s : std_logic;
	Signal RUT_sem_bloq_slp_Ruta_3_s : std_logic;
	begin
	enmascarador_inst:enmascarador port map(
		Clock => Clock,
		Reset => Reset,
		Modo => Modo,
		Ruta_in => Ruta_in,
		Circuito_de_via => cv_s,
		Semaforo_rojo_in => Semaforo_rojo_in,
		Semaforo_amarillo_in => Semaforo_amarillo_in,
		Semaforo_verde_in => Semaforo_verde_in,
		Barrera_alta_in => Barrera_alta_in,
		Barrera_baja_in => Barrera_baja_in,
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
		Estado_CV_bloq_Ruta_1 => Estado_CV_bloq_Ruta_1_s,
		Estado_ruta_bloq_Ruta_1 => Estado_ruta_bloq_Ruta_1_s,
		MDC_bloq_temp_solape_Ruta_1 => MDC_bloq_temp_solape_Ruta_1_s,
		Estado_ruta_Ruta_1 => Estado_ruta_Ruta_1_s,
		CV_alarma_total_Ruta_1 => CV_alarma_total_Ruta_1_s,
		CV_alarma_inmediata_Ruta_1 => CV_alarma_inmediata_Ruta_1_s,
		PAN_bloq_temp_solape_Ruta_1 => PAN_bloq_temp_solape_Ruta_1_s,
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
		Estado_CV_bloq_Ruta_2 => Estado_CV_bloq_Ruta_2_s,
		Estado_ruta_bloq_Ruta_2 => Estado_ruta_bloq_Ruta_2_s,
		MDC_bloq_temp_solape_Ruta_2 => MDC_bloq_temp_solape_Ruta_2_s,
		Estado_ruta_Ruta_2 => Estado_ruta_Ruta_2_s,
		CV_alarma_total_Ruta_2 => CV_alarma_total_Ruta_2_s,
		CV_alarma_inmediata_Ruta_2 => CV_alarma_inmediata_Ruta_2_s,
		PAN_bloq_temp_solape_Ruta_2 => PAN_bloq_temp_solape_Ruta_2_s,
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
		Estado_CV_bloq_Ruta_3 => Estado_CV_bloq_Ruta_3_s,
		Estado_ruta_bloq_Ruta_3 => Estado_ruta_bloq_Ruta_3_s,
		MDC_bloq_temp_solape_Ruta_3 => MDC_bloq_temp_solape_Ruta_3_s,
		Estado_ruta_Ruta_3 => Estado_ruta_Ruta_3_s,
		CV_alarma_total_Ruta_3 => CV_alarma_total_Ruta_3_s,
		CV_alarma_inmediata_Ruta_3 => CV_alarma_inmediata_Ruta_3_s,
		PAN_bloq_temp_solape_Ruta_3 => PAN_bloq_temp_solape_Ruta_3_s,
		Maquina_normal_in => Maquina_normal_in,
		Maquina_reversa_in => Maquina_reversa_in);
	cv_s <= Ocupacion;
	Rojo_in_s <= Semaforo_rojo_in;
	Amarillo_in_s <= Semaforo_amarillo_in;
	Verde_in_s <= Semaforo_verde_in;
	Semaforo_rojo_out <= Rojo_out_s;
	Semaforo_amarillo_out <= Amarillo_out_s;
	Semaforo_verde_out <= Verde_out_s;
	Alto_in_s <= Barrera_alta_in;
	Bajo_in_s <= Barrera_baja_in;
	Barrera_alta_out <= Alto_out_s;
	Barrera_baja_out <= Bajo_out_s;
	Maquina_normal_in_s <= Maquina_normal_in;
	Maquina_reversa_in_s <= Maquina_reversa_in;
	Maquina_normal_out <= Maquina_normal_out_s;
	Maquina_reversa_out <= Maquina_reversa_out_s;
	process(Clock,Reset)
	begin
		if (Clock ='1' and Clock'Event and Reset='1') then
			Reset_sem_s <= '0';
			Reset_pan_s <= '0';
		end if;
	end process;
end architecture unidad_central_enclavamiento_ARQ;
