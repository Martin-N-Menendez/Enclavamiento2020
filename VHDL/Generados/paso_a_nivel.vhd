-- paso_a_nivel.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad de paso_a_nivel
entity paso_a_nivel is
	port(
		Clock : in std_logic;
		Reset : in std_logic;
		Alto_in : in std_logic;
		Bajo_in : in std_logic;
		Alto_out : out std_logic;
		Bajo_out : out std_logic
	);
end entity paso_a_nivel;
-- Arquitectura del paso a nivel : Descripcion del comportamiento
architecture paso_a_nivel_ARQ of paso_a_nivel is
	begin
		process(Clock,Reset)
		begin
			if Reset='1' then
				Alto_out <= '0';
				Bajo_out <= '0';
			elsif (Clock ='1' and Clock'Event) then
				Alto_out <= Alto_in;
				Bajo_out <= Bajo_in;
			end if;
		end process;
end architecture paso_a_nivel_ARQ;
