-- mediador.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad de mediador
entity mediador is
	generic(
		N_CVS : natural := 3;
		N_SEM : natural := 3;
		N_PAN : natural := 1;
		N_MDC : natural := 2;
		N_RUT : natural := 3
	);
	port(
		Clock : in std_logic;
		Reset : in std_logic;
		SEM_rojo_Ruta_1 : in std_logic;
		SEM_naranja_Ruta_1 : in std_logic;
		SEM_doble_naranja_Ruta_1 : in std_logic;
		SEM_verde_Ruta_1 : in std_logic;
		MDC_normal_Ruta_1 : in std_logic;
		MDC_reverso_Ruta_1 : in std_logic;
		MDC_libre_Ruta_1 : in std_logic;
		MDC_cerrojado_Ruta_1 : in std_logic;
		PAN_alto_Ruta_1 : in std_logic;
		PAN_bajo_Ruta_1 : in std_logic;
		PAN_alarma_Ruta_1 : in std_logic;
		PAN_habilitacion_Ruta_1 : in std_logic;
		RUT_estado_Ruta_1 : in std_logic;
		RUT_sem_bloq_slp_Ruta_1 : in std_logic;
		SEM_rojo_Ruta_2 : in std_logic;
		SEM_naranja_Ruta_2 : in std_logic;
		SEM_doble_naranja_Ruta_2 : in std_logic;
		SEM_verde_Ruta_2 : in std_logic;
		MDC_normal_Ruta_2 : in std_logic;
		MDC_reverso_Ruta_2 : in std_logic;
		MDC_libre_Ruta_2 : in std_logic;
		MDC_cerrojado_Ruta_2 : in std_logic;
		PAN_alto_Ruta_2 : in std_logic;
		PAN_bajo_Ruta_2 : in std_logic;
		PAN_alarma_Ruta_2 : in std_logic;
		PAN_habilitacion_Ruta_2 : in std_logic;
		RUT_estado_Ruta_2 : in std_logic;
		RUT_sem_bloq_slp_Ruta_2 : in std_logic;
		SEM_rojo_Ruta_3 : in std_logic;
		SEM_naranja_Ruta_3 : in std_logic;
		SEM_doble_naranja_Ruta_3 : in std_logic;
		SEM_verde_Ruta_3 : in std_logic;
		MDC_normal_Ruta_3 : in std_logic;
		MDC_reverso_Ruta_3 : in std_logic;
		MDC_libre_Ruta_3 : in std_logic;
		MDC_cerrojado_Ruta_3 : in std_logic;
		PAN_alto_Ruta_3 : in std_logic;
		PAN_bajo_Ruta_3 : in std_logic;
		PAN_alarma_Ruta_3 : in std_logic;
		PAN_habilitacion_Ruta_3 : in std_logic;
		RUT_estado_Ruta_3 : in std_logic;
		RUT_sem_bloq_slp_Ruta_3 : in std_logic;
		Semaforo_rojo : out std_logic_vector(N_SEM-1 downto 0);
		Semaforo_amarillo : out std_logic_vector(N_SEM-1 downto 0);
		Semaforo_verde : out std_logic_vector(N_SEM-1 downto 0);
		Barrera_baja : out std_logic_vector(N_PAN-1 downto 0);
		Barrera_alta : out std_logic_vector(N_PAN-1 downto 0);
		Maquina_normal : out std_logic_vector(N_MDC-1 downto 0);
		Maquina_reversa : out std_logic_vector(N_MDC-1 downto 0)
	);
end entity mediador;
-- Arquitectura del señalamiento : Descripcion del comportamiento
architecture mediador_ARQ of mediador is
	Signal Rojo_in_s,Amarillo_in_s,Verde_in_s,Rojo_out_s,Amarillo_out_s,Verde_out_s: std_logic_vector(N_SEM-1 downto 0);
	Signal Alto_in_s,Bajo_in_s,Alto_out_s,Bajo_out_s: std_logic_vector(N_PAN-1 downto 0);
	Signal Maquina_normal_in_s,Maquina_reversa_in_s,Maquina_normal_out_s,Maquina_reversa_out_s: std_logic_vector(N_MDC-1 downto 0);
	Signal Reset_sem_s,Reset_Pan_s: std_logic;
	begin
	process(Clock,Reset)
	begin
		if (Clock ='1' and Clock'Event and Reset='1') then
			Barrera_alta(0) <= PAN_alto_Ruta_1 or PAN_habilitacion_Ruta_1;
			Barrera_baja(0) <= PAN_bajo_Ruta_1 or PAN_habilitacion_Ruta_1;
			Maquina_normal(0) <= MDC_normal_Ruta_1 or MDC_libre_Ruta_1 or MDC_cerrojado_Ruta_1;
			Maquina_reversa(0) <= MDC_reverso_Ruta_1 or MDC_libre_Ruta_1 or MDC_cerrojado_Ruta_1;
			Maquina_normal(1) <= MDC_normal_Ruta_2 or MDC_libre_Ruta_2 or MDC_cerrojado_Ruta_2;
			Maquina_reversa(1) <= MDC_reverso_Ruta_2 or MDC_libre_Ruta_2 or MDC_cerrojado_Ruta_2;
			Semaforo_rojo(0) <= SEM_rojo_Ruta_1;
			Semaforo_amarillo(0) <= SEM_naranja_Ruta_1 or SEM_doble_naranja_Ruta_1;
			Semaforo_verde(0) <= SEM_verde_Ruta_1;
			Semaforo_rojo(1) <= SEM_rojo_Ruta_2;
			Semaforo_amarillo(1) <= SEM_naranja_Ruta_2 or SEM_doble_naranja_Ruta_2;
			Semaforo_verde(1) <= SEM_verde_Ruta_2;
			Semaforo_rojo(2) <= SEM_rojo_Ruta_3;
			Semaforo_amarillo(2) <= SEM_naranja_Ruta_3 or SEM_doble_naranja_Ruta_3;
			Semaforo_verde(2) <= SEM_verde_Ruta_3;
		end if;
	end process;
end architecture mediador_ARQ;
