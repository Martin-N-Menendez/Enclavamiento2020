-- pan_fsm_3.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad_3 de pan_fsm
entity pan_fsm_3 is
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
end entity pan_fsm_3;
-- Arquitectura de FSM_barreras_3 : Descripcion del comportamiento
architecture pan_fsm_3_ARQ of pan_fsm_3 is
	begin
	process(Clock,Reset)
	begin
		if (Clock ='1' and Clock'Event) then
			PAN_alarma_Ruta_3 <= CV_alarma_inmediata_Ruta_3(1) or CV_alarma_inmediata_Ruta_3(2) or CV_alarma_inmediata_Ruta_3(3);
			PAN_alto_Ruta_3 <= CV_alarma_total_Ruta_3(1) or CV_alarma_total_Ruta_3(2) or CV_alarma_total_Ruta_3(3);
			PAN_bajo_Ruta_3 <= Estado_ruta_Ruta_3(1) or Estado_ruta_Ruta_3(2) or Estado_ruta_Ruta_3(3);
			PAN_habilitacion_Ruta_3 <= PAN_bloq_temp_solape_Ruta_3(1) or PAN_bloq_temp_solape_Ruta_3(2) or PAN_bloq_temp_solape_Ruta_3(3);
		end if;
	end process;
end architecture pan_fsm_3_ARQ;
