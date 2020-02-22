-- mediador.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity mediador is
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
			Cambios :  in std_logic_vector(1-1 downto 0);
			Salida :  out std_logic_vector(28-1 downto 0)
		);
	end entity mediador;
architecture Behavioral of mediador is
begin
	process(Clock,Reset)
	begin
		if (Clock = '1' and Clock'Event) then
			if (Reset = '1') then
				Salida <= "0000000000000000000000000000";
			else
				Salida(0) <= semaforos.lsb(0);
				Salida(1) <= semaforos.msb(0);
				Salida(2) <= semaforos.lsb(1);
				Salida(3) <= semaforos.msb(1);
				Salida(4) <= semaforos.lsb(2);
				Salida(5) <= semaforos.msb(2);
				Salida(6) <= semaforos.lsb(3);
				Salida(7) <= semaforos.msb(3);
				Salida(8) <= semaforos.lsb(4);
				Salida(9) <= semaforos.msb(4);
				Salida(10) <= semaforos.lsb(5);
				Salida(11) <= semaforos.msb(5);
				Salida(12) <= semaforos.lsb(6);
				Salida(13) <= semaforos.msb(6);
				Salida(14) <= semaforos.lsb(7);
				Salida(15) <= semaforos.msb(7);
				Salida(16) <= semaforos.lsb(8);
				Salida(17) <= semaforos.msb(8);
				Salida(18) <= semaforos.lsb(9);
				Salida(19) <= semaforos.msb(9);
				Salida(20) <= semaforos.lsb(10);
				Salida(21) <= semaforos.msb(10);
				Salida(22) <= semaforos.lsb(11);
				Salida(23) <= semaforos.msb(11);
				Salida (27-1 downto 24) <= barreras;
				Salida (28-1 downto 27) <= Cambios;
			end if;
		end if;
	end process;
end Behavioral;
