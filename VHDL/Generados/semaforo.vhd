-- semaforo.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad de semaforo
entity semaforo is
	port(
		Clock : in std_logic;
		Reset : in std_logic;
		Rojo_in : in std_logic;
		Amarillo_in : in std_logic;
		Verde_in : in std_logic;
		Rojo_out : out std_logic;
		Amarillo_out : out std_logic;
		Verde_out : out std_logic
	);
end entity semaforo;
-- Arquitectura del paso a nivel : Descripcion del comportamiento
architecture semaforo_ARQ of semaforo is
	begin
		process(Clock,Reset)
		begin
			if Reset='1' then
				Rojo_out <= '0';
				Amarillo_out <= '0';
				Verde_out <= '0';
			elsif (Clock ='1' and Clock'Event) then
				Rojo_out <= Rojo_in;
				Amarillo_out <= Amarillo_in;
				Verde_out <= Verde_in;
			end if;
		end process;
end architecture semaforo_ARQ;
