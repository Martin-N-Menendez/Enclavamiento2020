-- mdc_fsm_1.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad_1 de mdc_fsm
entity mdc_fsm_1 is
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
end entity mdc_fsm_1;
-- Arquitectura de FSM_cambios_1 : Descripcion del comportamiento
architecture mdc_fsm_1_ARQ of mdc_fsm_1 is
	begin
	process(Clock,Reset)
	begin
		if (Clock ='1' and Clock'Event) then
			MDC_cerrojado_Ruta_1 <= Estado_ruta_bloq_Ruta_1(1) or Estado_ruta_bloq_Ruta_1(2) or Estado_ruta_bloq_Ruta_1(3);
			MDC_libre_Ruta_1 <= MDC_bloq_temp_solape_Ruta_1(1) or MDC_bloq_temp_solape_Ruta_1(2) or MDC_bloq_temp_solape_Ruta_1(3);
			MDC_normal_Ruta_1 <= Estado_CV_bloq_Ruta_1 or MDC_bloq_temp_solape_Ruta_1(2) or Estado_ruta_bloq_Ruta_1(3);
			MDC_reverso_Ruta_1 <= Estado_CV_bloq_Ruta_1;
		end if;
	end process;
end architecture mdc_fsm_1_ARQ;
