-- cambios.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad de cambios
entity cambios is
	generic(
		N_MDC : natural := 2
	);
	port(
		Clock : in std_logic;
		Reset : in std_logic;
		Maquina_normal_in : in std_logic_vector(N_MDC-1 downto 0);
		Maquina_reversa_in : in std_logic_vector(N_MDC-1 downto 0);
		Maquina_normal_out : out std_logic_vector(N_MDC-1 downto 0);
		Maquina_reversa_out : out std_logic_vector(N_MDC-1 downto 0)
	);
end entity cambios;
-- Arquitectura de los cambios ferroviarios : Descripcion del comportamiento
architecture cambios_ARQ of cambios is
	--componente de cambio
	component cambio is
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			Maquina_normal_in : in std_logic;
			Maquina_reversa_in : in std_logic;
			Maquina_normal_out : out std_logic;
			Maquina_reversa_out : out std_logic
		);
	end component cambio;
	begin
		cambio_i: for i in 0 to N_MDC-1 generate
			cambio_inst:cambio port map(
				Clock => Clock,
				Reset => Reset,
				Maquina_normal_in => Maquina_normal_in(i),
				Maquina_reversa_in => Maquina_reversa_in(i),
				Maquina_normal_out => Maquina_normal_out(i),
				Maquina_reversa_out => Maquina_reversa_out(i));
		end generate;
end architecture cambios_ARQ;
