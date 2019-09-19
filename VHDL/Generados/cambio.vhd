-- cambio.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad de cambio
entity cambio is
	port(
		Clock : in std_logic;
		Reset : in std_logic;
		Maquina_normal_in : in std_logic;
		Maquina_reversa_in : in std_logic;
		Maquina_normal_out : out std_logic;
		Maquina_reversa_out : out std_logic
	);
end entity cambio;
-- Arquitectura del cambio ferroviario : Descripcion del comportamiento
architecture cambio_ARQ of cambio is
	begin
		process(Clock,Reset)
		begin
			if Reset='1' then
				Maquina_normal_out <= '0';
				Maquina_reversa_out <= '0';
			elsif (Clock ='1' and Clock'Event) then
				Maquina_normal_out <= Maquina_normal_in;
				Maquina_reversa_out <= Maquina_reversa_in;
			end if;
		end process;
end architecture cambio_ARQ;
