-- rut_fsm_2.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad_2 de rut_fsm
entity rut_fsm_2 is
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
end entity rut_fsm_2;
-- Arquitectura de FSM_rutas2 : Descripcion del comportamiento
architecture rut_fsm_2_ARQ of rut_fsm_2 is
	begin
	process(Clock,Reset)
	begin
		if (Clock ='1' and Clock'Event) then
			RUT_estado_Ruta_2 <= Bloq_MDC_ruta_Ruta_2(1) or Bloq_MDC_solape_Ruta_2(1) or CV_aprox_Ruta_2(1) or CV_despeje_Ruta_2(1) or CV_int_Ruta_2 or CV_paralelo_Ruta_2(1) or CV_paralelo_temp_Ruta_2(1);
			RUT_sem_bloq_slp_Ruta_2 <= Estado_PAN_Ruta_2(1) or Estado_SEM_sgte_Ruta_2(1) or Estado_ruta_cond_Ruta_2(1) or Estado_ruta_confl_Ruta_2(1) or Estado_sub_ruta_Ruta_2(1) or Pos_MDC_aprox_Ruta_2(1) or Pos_MDC_despeje_Ruta_2(1);
			SEM_estado_Ruta_2 <= Pos_MDC_ruta_Ruta_2(1) or Pos_MDC_solape_Ruta_2(1) or Estado_SEM_sgte_Ruta_2(1) or Estado_ruta_confl_Ruta_2(1) or CV_int_Ruta_2 or CV_despeje_Ruta_2(1) or Bloq_MDC_ruta_Ruta_2(1);
		end if;
	end process;
end architecture rut_fsm_2_ARQ;
