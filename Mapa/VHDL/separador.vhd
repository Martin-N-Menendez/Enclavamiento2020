-- separador.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity separador is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Paquete :  in std_logic_vector(N-1 downto 0);
			Ocupacion :  out std_logic_vector(N_CVS-1 downto 0);
			semaforos :  out sems_type;
			Cambios :  out std_logic_vector(N_MDC-1 downto 0);
			Reset :  in std_logic
		);
	end entity separador;
architecture Behavioral of separador is
	Signal cv_s : std_logic_vector(N_CVS-1 downto 0);
	Signal sem_s_i,sem_s_o : sems_type;
	Signal mdc_s_i,mdc_s_o : std_logic_vector(N_MDC-1 downto 0);
begin
	process(Clock,Reset)
	begin
		if (Clock = '1' and Clock'Event) then
			if (Reset = '1') then
				Ocupacion <= "000000000000000000000000000000000";
				semaforos.lsb <= "000000000000000000000000000000000000";
				semaforos.msb <= "000000000000000000000000000000000000";
				Cambios <= "00000000000000";
			else
				Ocupacion <= Paquete(33-1 downto 0);
				semaforos.msb(0) <= Paquete(33);
				semaforos.lsb(0) <= Paquete(34);
				semaforos.msb(1) <= Paquete(35);
				semaforos.lsb(1) <= Paquete(36);
				semaforos.msb(2) <= Paquete(37);
				semaforos.lsb(2) <= Paquete(38);
				semaforos.msb(3) <= Paquete(39);
				semaforos.lsb(3) <= Paquete(40);
				semaforos.msb(4) <= Paquete(41);
				semaforos.lsb(4) <= Paquete(42);
				semaforos.msb(5) <= Paquete(43);
				semaforos.lsb(5) <= Paquete(44);
				semaforos.msb(6) <= Paquete(45);
				semaforos.lsb(6) <= Paquete(46);
				semaforos.msb(7) <= Paquete(47);
				semaforos.lsb(7) <= Paquete(48);
				semaforos.msb(8) <= Paquete(49);
				semaforos.lsb(8) <= Paquete(50);
				semaforos.msb(9) <= Paquete(51);
				semaforos.lsb(9) <= Paquete(52);
				semaforos.msb(10) <= Paquete(53);
				semaforos.lsb(10) <= Paquete(54);
				semaforos.msb(11) <= Paquete(55);
				semaforos.lsb(11) <= Paquete(56);
				semaforos.msb(12) <= Paquete(57);
				semaforos.lsb(12) <= Paquete(58);
				semaforos.msb(13) <= Paquete(59);
				semaforos.lsb(13) <= Paquete(60);
				semaforos.msb(14) <= Paquete(61);
				semaforos.lsb(14) <= Paquete(62);
				semaforos.msb(15) <= Paquete(63);
				semaforos.lsb(15) <= Paquete(64);
				semaforos.msb(16) <= Paquete(65);
				semaforos.lsb(16) <= Paquete(66);
				semaforos.msb(17) <= Paquete(67);
				semaforos.lsb(17) <= Paquete(68);
				semaforos.msb(18) <= Paquete(69);
				semaforos.lsb(18) <= Paquete(70);
				semaforos.msb(19) <= Paquete(71);
				semaforos.lsb(19) <= Paquete(72);
				semaforos.msb(20) <= Paquete(73);
				semaforos.lsb(20) <= Paquete(74);
				semaforos.msb(21) <= Paquete(75);
				semaforos.lsb(21) <= Paquete(76);
				semaforos.msb(22) <= Paquete(77);
				semaforos.lsb(22) <= Paquete(78);
				semaforos.msb(23) <= Paquete(79);
				semaforos.lsb(23) <= Paquete(80);
				semaforos.msb(24) <= Paquete(81);
				semaforos.lsb(24) <= Paquete(82);
				semaforos.msb(25) <= Paquete(83);
				semaforos.lsb(25) <= Paquete(84);
				semaforos.msb(26) <= Paquete(85);
				semaforos.lsb(26) <= Paquete(86);
				semaforos.msb(27) <= Paquete(87);
				semaforos.lsb(27) <= Paquete(88);
				semaforos.msb(28) <= Paquete(89);
				semaforos.lsb(28) <= Paquete(90);
				semaforos.msb(29) <= Paquete(91);
				semaforos.lsb(29) <= Paquete(92);
				semaforos.msb(30) <= Paquete(93);
				semaforos.lsb(30) <= Paquete(94);
				semaforos.msb(31) <= Paquete(95);
				semaforos.lsb(31) <= Paquete(96);
				semaforos.msb(32) <= Paquete(97);
				semaforos.lsb(32) <= Paquete(98);
				semaforos.msb(33) <= Paquete(99);
				semaforos.lsb(33) <= Paquete(100);
				semaforos.msb(34) <= Paquete(101);
				semaforos.lsb(34) <= Paquete(102);
				semaforos.msb(35) <= Paquete(103);
				semaforos.lsb(35) <= Paquete(104);
				Cambios <= Paquete(119-1 downto 105);
			end if;
		end if;
	end process;
end Behavioral;
