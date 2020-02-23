-- separador.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity separador is
		generic(
			N : natural := 39;
			N_SEM : natural := 12;
			N_MDC : natural := 2;
			N_CVS : natural := 13
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
				Ocupacion <= "0000000000000";
				semaforos.lsb <= "000000000000";
				semaforos.msb <= "000000000000";
				Cambios <= "00";
			else
				Ocupacion <= Paquete(13-1 downto 0);
				semaforos.msb(0) <= Paquete(13);
				semaforos.lsb(0) <= Paquete(14);
				semaforos.msb(1) <= Paquete(15);
				semaforos.lsb(1) <= Paquete(16);
				semaforos.msb(2) <= Paquete(17);
				semaforos.lsb(2) <= Paquete(18);
				semaforos.msb(3) <= Paquete(19);
				semaforos.lsb(3) <= Paquete(20);
				semaforos.msb(4) <= Paquete(21);
				semaforos.lsb(4) <= Paquete(22);
				semaforos.msb(5) <= Paquete(23);
				semaforos.lsb(5) <= Paquete(24);
				semaforos.msb(6) <= Paquete(25);
				semaforos.lsb(6) <= Paquete(26);
				semaforos.msb(7) <= Paquete(27);
				semaforos.lsb(7) <= Paquete(28);
				semaforos.msb(8) <= Paquete(29);
				semaforos.lsb(8) <= Paquete(30);
				semaforos.msb(9) <= Paquete(31);
				semaforos.lsb(9) <= Paquete(32);
				semaforos.msb(10) <= Paquete(33);
				semaforos.lsb(10) <= Paquete(34);
				semaforos.msb(11) <= Paquete(35);
				semaforos.lsb(11) <= Paquete(36);
				Cambios <= Paquete(39-1 downto 37);
			end if;
		end if;
	end process;
end Behavioral;
