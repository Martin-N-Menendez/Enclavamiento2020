-- sem_fsm_2.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad_2 de sem_fsm
entity sem_fsm_2 is
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
end entity sem_fsm_2;
-- Arquitectura de FSM_semaforos2 : Descripcion del comportamiento
architecture sem_fsm_2_ARQ of sem_fsm_2 is
	begin
	process(Clock,Reset)
	begin
		if (Clock ='1' and Clock'Event) then
			if Reset ='1' then
			SEM_rojo_Ruta_2 <= '0';
			SEM_doble_naranja_Ruta_2 <= '0';
			SEM_naranja_Ruta_2 <= '0';
			SEM_verde_Ruta_2 <= '0';
			else
				SEM_rojo_Ruta_2 <= SEM_estado_Ruta_2;
				SEM_doble_naranja_Ruta_2 <= not SEM_estado_Ruta_2;
				SEM_naranja_Ruta_2 <= SEM_estado_Ruta_2;
				SEM_verde_Ruta_2 <= not SEM_estado_Ruta_2;
			end if;
		end if;
	end process;
end architecture sem_fsm_2_ARQ;
