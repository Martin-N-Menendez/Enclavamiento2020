-- separador.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity separador is
		generic(
			N : natural := 32;
			N_SEM : natural := 10;
			N_MDC : natural := 2;
			N_CVS : natural := 10
		);
		port(
			Clock :  in std_logic;
			Paquete :  in std_logic_vector(N-1 downto 0);
			procesar :  in std_logic;
			procesado :  out std_logic;
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
				Ocupacion <= "0000000000";
				semaforos.lsb <= "0000000000";
				semaforos.msb <= "0000000000";
				Cambios <= "00";
				procesado <= '0';
			else
				procesado <= procesar;
				if procesar = '1' then
					Ocupacion(0) <= Paquete(31);
					Ocupacion(1) <= Paquete(30);
					Ocupacion(2) <= Paquete(29);
					Ocupacion(3) <= Paquete(28);
					Ocupacion(4) <= Paquete(27);
					Ocupacion(5) <= Paquete(26);
					Ocupacion(6) <= Paquete(25);
					Ocupacion(7) <= Paquete(24);
					Ocupacion(8) <= Paquete(23);
					Ocupacion(9) <= Paquete(22);
					semaforos.msb(0) <= Paquete(21);
					semaforos.lsb(0) <= Paquete(20);
					semaforos.msb(1) <= Paquete(19);
					semaforos.lsb(1) <= Paquete(18);
					semaforos.msb(2) <= Paquete(17);
					semaforos.lsb(2) <= Paquete(16);
					semaforos.msb(3) <= Paquete(15);
					semaforos.lsb(3) <= Paquete(14);
					semaforos.msb(4) <= Paquete(13);
					semaforos.lsb(4) <= Paquete(12);
					semaforos.msb(5) <= Paquete(11);
					semaforos.lsb(5) <= Paquete(10);
					semaforos.msb(6) <= Paquete(9);
					semaforos.lsb(6) <= Paquete(8);
					semaforos.msb(7) <= Paquete(7);
					semaforos.lsb(7) <= Paquete(6);
					semaforos.msb(8) <= Paquete(5);
					semaforos.lsb(8) <= Paquete(4);
					semaforos.msb(9) <= Paquete(3);
					semaforos.lsb(9) <= Paquete(2);
					Cambios(0) <= Paquete(1);
					Cambios(1) <= Paquete(0);
				end if;
			end if;
		end if;
	end process;
end Behavioral;