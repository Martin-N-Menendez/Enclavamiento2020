-- sistema.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity sistema is
		generic(
			N : natural := 39;
			N_SEM : natural := 12;
			N_MDC : natural := 2;
			N_CVS : natural := 13
		);
		port(
			Clock :  in std_logic;
			Paquete_i :  in std_logic_vector(39-1 downto 0);
			Paquete_o :  out std_logic_vector(26-1 downto 0);
			Reset :  in std_logic
		);
	end entity sistema;
architecture Behavioral of sistema is
	component separador is
		generic(
			N : natural := 39;
			N_SEM : natural := 12;
			N_MDC : natural := 2;
			N_CVS : natural := 13
		);
		port(
			Clock :  in std_logic;
			Paquete :  in std_logic_vector(39-1 downto 0);
			Ocupacion :  out std_logic_vector(13-1 downto 0);
			semaforos :  out sems_type;
			Cambios :  out std_logic_vector(2-1 downto 0);
			Reset :  in std_logic
		);
	end component separador;
	component red is
		generic(
			N : natural := 39;
			N_SEM : natural := 12;
			N_MDC : natural := 2;
			N_CVS : natural := 13
		);
		port(
			Clock :  in std_logic;
			Ocupacion :  in std_logic_vector(13-1 downto 0);
			semaforos_i :  in sems_type;
			semaforos_o :  out sems_type;
			Cambios_i :  in std_logic_vector(2-1 downto 0);
			Cambios_o :  out std_logic_vector(2-1 downto 0);
			Reset :  in std_logic
		);
	end component red;
	component mediador is
		generic(
			N : natural := 39;
			N_CVS : natural := 13;
			N_SEM : natural := 12;
			N_PAN : natural := 0;
			N_MDC : natural := 2
		);
		port(
			Clock :  in std_logic;
			semaforos :  in sems_type;
			Cambios :  in std_logic_vector(2-1 downto 0);
			Salida :  out std_logic_vector(26-1 downto 0);
			Reset :  in std_logic
		);
	end component mediador;
	Signal cv_s : std_logic_vector(N_CVS-1 downto 0);
	Signal sem_s_i,sem_s_o : sems_type;
	Signal mdc_s_i,mdc_s_o : std_logic_vector(N_MDC-1 downto 0);

begin
	separador_i:separador port map(
		Clock => Clock,
		Paquete => Paquete_i,
		Ocupacion => cv_s,
		semaforos => sem_s_i,
		Cambios => mdc_s_i,
		Reset => Reset
		);
	mediador_i:mediador port map(
		Clock => Clock,
		semaforos => sem_s_o,
		Cambios => mdc_s_o,
		Salida => Paquete_o,
		Reset => Reset
		);
	red_i:red port map(
		Clock => Clock,
		Ocupacion => cv_s,
		semaforos_i => sem_s_i,
		semaforos_o => sem_s_o,
		Cambios_i => mdc_s_i,
		Cambios_o => mdc_s_o,
		Reset => Reset
		);
end Behavioral;
