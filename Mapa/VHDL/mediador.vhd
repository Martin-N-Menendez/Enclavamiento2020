-- mediador.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity mediador is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			semaforos :  in sems_type;
			Cambios :  in std_logic_vector(14-1 downto 0);
			Salida :  out std_logic_vector(86-1 downto 0);
			Reset :  in std_logic
		);
	end entity mediador;
architecture Behavioral of mediador is
begin
	process(Clock,Reset)
	begin
		if (Clock = '1' and Clock'Event) then
			if (Reset = '1') then
				Salida <= "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000";
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
				Salida(24) <= semaforos.lsb(12);
				Salida(25) <= semaforos.msb(12);
				Salida(26) <= semaforos.lsb(13);
				Salida(27) <= semaforos.msb(13);
				Salida(28) <= semaforos.lsb(14);
				Salida(29) <= semaforos.msb(14);
				Salida(30) <= semaforos.lsb(15);
				Salida(31) <= semaforos.msb(15);
				Salida(32) <= semaforos.lsb(16);
				Salida(33) <= semaforos.msb(16);
				Salida(34) <= semaforos.lsb(17);
				Salida(35) <= semaforos.msb(17);
				Salida(36) <= semaforos.lsb(18);
				Salida(37) <= semaforos.msb(18);
				Salida(38) <= semaforos.lsb(19);
				Salida(39) <= semaforos.msb(19);
				Salida(40) <= semaforos.lsb(20);
				Salida(41) <= semaforos.msb(20);
				Salida(42) <= semaforos.lsb(21);
				Salida(43) <= semaforos.msb(21);
				Salida(44) <= semaforos.lsb(22);
				Salida(45) <= semaforos.msb(22);
				Salida(46) <= semaforos.lsb(23);
				Salida(47) <= semaforos.msb(23);
				Salida(48) <= semaforos.lsb(24);
				Salida(49) <= semaforos.msb(24);
				Salida(50) <= semaforos.lsb(25);
				Salida(51) <= semaforos.msb(25);
				Salida(52) <= semaforos.lsb(26);
				Salida(53) <= semaforos.msb(26);
				Salida(54) <= semaforos.lsb(27);
				Salida(55) <= semaforos.msb(27);
				Salida(56) <= semaforos.lsb(28);
				Salida(57) <= semaforos.msb(28);
				Salida(58) <= semaforos.lsb(29);
				Salida(59) <= semaforos.msb(29);
				Salida(60) <= semaforos.lsb(30);
				Salida(61) <= semaforos.msb(30);
				Salida(62) <= semaforos.lsb(31);
				Salida(63) <= semaforos.msb(31);
				Salida(64) <= semaforos.lsb(32);
				Salida(65) <= semaforos.msb(32);
				Salida(66) <= semaforos.lsb(33);
				Salida(67) <= semaforos.msb(33);
				Salida(68) <= semaforos.lsb(34);
				Salida(69) <= semaforos.msb(34);
				Salida(70) <= semaforos.lsb(35);
				Salida(71) <= semaforos.msb(35);
				Salida (86-1 downto 72) <= Cambios;
			end if;
		end if;
	end process;
end Behavioral;
