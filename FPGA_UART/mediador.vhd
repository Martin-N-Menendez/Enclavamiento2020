-- mediador.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity mediador is
		generic(
			N : natural := 23;
			N_CVS : natural := 6;
			N_SEM : natural := 7;
			N_PAN : natural := 2;
			N_MDC : natural := 1
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			semaforos :  in sems_type;
			barreras :  in std_logic_vector(2-1 downto 0);
			Cambios :  in std_logic_vector(1-1 downto 0);
			Salida :  out std_logic_vector(17-1 downto 0)
		);
	end entity mediador;
architecture Behavioral of mediador is
begin
	process(Clock,Reset)
	begin
		if (Clock = '1' and Clock'Event) then
			if (Reset = '1') then
				Salida <= "00000000000000000";
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
				Salida (16-1 downto 14) <= barreras;
				Salida (17-1 downto 16) <= Cambios;
			end if;
		end if;
	end process;
end Behavioral;
