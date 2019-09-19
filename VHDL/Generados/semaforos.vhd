-- semaforos.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad de semaforos
entity semaforos is
	generic(
		N_SEM : natural := 3
	);
	port(
		Clock : in std_logic;
		Reset : in std_logic;
		Rojo_in : in std_logic_vector(N_SEM-1 downto 0);
		Amarillo_in : in std_logic_vector(N_SEM-1 downto 0);
		Verde_in : in std_logic_vector(N_SEM-1 downto 0);
		Rojo_out : out std_logic_vector(N_SEM-1 downto 0);
		Amarillo_out : out std_logic_vector(N_SEM-1 downto 0);
		Verde_out : out std_logic_vector(N_SEM-1 downto 0)
	);
end entity semaforos;
-- Arquitectura de los semaforos : Descripcion del comportamiento
architecture semaforos_ARQ of semaforos is
	--componente de semaforo
	component semaforo is
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
	end component semaforo;
	begin
		semaforo_i: for i in 0 to N_SEM-1 generate
			semaforo_inst:semaforo port map(
				Clock => Clock,
				Reset => Reset,
				Rojo_in => Rojo_in(i),
				Amarillo_in => Amarillo_in(i),
				Verde_in => Verde_in(i),
				Rojo_out => Rojo_out(i),
				Amarillo_out => Amarillo_out(i),
				Verde_out => Verde_out(i));
		end generate;
end architecture semaforos_ARQ;
