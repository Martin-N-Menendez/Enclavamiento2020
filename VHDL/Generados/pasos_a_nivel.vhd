-- pasos_a_nivel.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad de pasos_a_nivel
entity pasos_a_nivel is
	generic(
		N_PAN : natural := 1
	);
	port(
		Clock : in std_logic;
		Reset : in std_logic;
		Alto_in : in std_logic_vector(N_PAN-1 downto 0);
		Bajo_in : in std_logic_vector(N_PAN-1 downto 0);
		Alto_out : out std_logic_vector(N_PAN-1 downto 0);
		Bajo_out : out std_logic_vector(N_PAN-1 downto 0)
	);
end entity pasos_a_nivel;
-- Arquitectura de los pasos a nivel : Descripcion del comportamiento
architecture pasos_a_nivel_ARQ of pasos_a_nivel is
	--componente de paso_a_nivel
	component paso_a_nivel is
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			Alto_in : in std_logic;
			Bajo_in : in std_logic;
			Alto_out : out std_logic;
			Bajo_out : out std_logic
		);
	end component paso_a_nivel;
	begin
		paso_a_nivel_i: for i in 0 to N_PAN-1 generate
			paso_a_nivel_inst:paso_a_nivel port map(
				Clock => Clock,
				Reset => Reset,
				Alto_in => Alto_in(i),
				Bajo_in => Bajo_in(i),
				Alto_out => Alto_out(i),
				Bajo_out => Bajo_out(i));
		end generate;
end architecture pasos_a_nivel_ARQ;
