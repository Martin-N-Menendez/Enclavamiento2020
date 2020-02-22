-- sistema.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity wrapper is
		generic(
			N : natural := 41;
			N_CVS : natural := 13;
			N_SEM : natural := 12;
			N_PAN : natural := 3;
			N_MDC : natural := 1
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Paquete_i :  in std_logic_vector(41-1 downto 0);
			Paquete_o :  out std_logic_vector(28-1 downto 0)
		);
	end entity wrapper;
architecture Behavioral of wrapper is
	component separador is
		generic(
			N : natural := 41;
			N_CVS : natural := 13;
			N_SEM : natural := 12;
			N_PAN : natural := 3;
			N_MDC : natural := 1
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Paquete :  in std_logic_vector(41-1 downto 0);
			Ocupacion :  out std_logic_vector(13-1 downto 0);
			semaforos :  out sems_type;
			barreras :  out std_logic_vector(3-1 downto 0);
			Cambios :  out std_logic
		);
	end component separador;
	component red is
		generic(
			N : natural := 41;
			N_CVS : natural := 13;
			N_SEM : natural := 12;
			N_PAN : natural := 3;
			N_MDC : natural := 1
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Ocupacion :  in std_logic_vector(13-1 downto 0);
			semaforos_i :  in sems_type;
			semaforos_o :  out sems_type;
			barreras_i :  in std_logic_vector(3-1 downto 0);
			barreras_o :  out std_logic_vector(3-1 downto 0);
			Cambios_i :  in std_logic;
			Cambios_o :  out std_logic
		);
	end component red;
	component mediador is
		generic(
			N : natural := 41;
			N_CVS : natural := 13;
			N_SEM : natural := 12;
			N_PAN : natural := 3;
			N_MDC : natural := 1
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			semaforos :  in sems_type;
			barreras :  in std_logic_vector(3-1 downto 0);
			Cambios :  in std_logic;
			Salida :  out std_logic_vector(28-1 downto 0)
		);
	end component mediador;
	Signal cv_s : std_logic_vector(N_CVS-1 downto 0);
	Signal sem_s_i,sem_s_o : sems_type;
	Signal pan_s_i,pan_s_o : std_logic_vector(N_PAN-1 downto 0);
	Signal mdc_s_i,mdc_s_o : std_logic;
begin
	separador_i:separador port map(
		Clock => Clock,
		Reset => Reset,
		Paquete => Paquete_i,
		Ocupacion => cv_s,
		semaforos => sem_s_i,
		barreras => pan_s_i,
		Cambios => mdc_s_i
		);
	mediador_i:mediador port map(
		Clock => Clock,
		Reset => Reset,
		semaforos => sem_s_o,
		barreras => pan_s_o,
		Cambios => mdc_s_o,
		Salida => Paquete_o
		);
	red_i:red port map(
		Clock => Clock,
		Reset => Reset,
		Ocupacion => cv_s,
		semaforos_i => sem_s_i,
		semaforos_o => sem_s_o,
		barreras_i => pan_s_i,
		barreras_o => pan_s_o,
		Cambios_i => mdc_s_i,
		Cambios_o => mdc_s_o
		);
end Behavioral;
