-- separador.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity separador is
		generic(
			N : natural := 21;
			N_SEM : natural := 7;
			N_MDC : natural := 1;
			N_CVS : natural := 6
		);
		port(
			Clock :  in std_logic;
			Paquete :  in std_logic_vector(N-1 downto 0);
			procesar :  in std_logic;
			procesado :  out std_logic;
			Ocupacion :  out std_logic_vector(N_CVS-1 downto 0);
			semaforos :  out sems_type;
			Cambios :  out std_logic;
			Reset :  in std_logic
		);
	end entity separador;
architecture Behavioral of separador is
	Signal cv_s : std_logic_vector(N_CVS-1 downto 0);
	Signal sem_s_i,sem_s_o : sems_type;
	Signal mdc_s_i,mdc_s_o : std_logic;
begin
	process(Clock,Reset)
	begin
		if (Clock = '1' and Clock'Event) then
			if (Reset = '1') then
				Ocupacion <= "000000";
				semaforos.lsb <= "0000000";
				semaforos.msb <= "0000000";
				Cambios <= '0';
				procesado <= '0';
			else
				procesado <= procesar;
				if procesar = '1' then
					Ocupacion <= Paquete(21-1 downto 16-1);
					semaforos.msb(0) <= Paquete(14);
					semaforos.lsb(0) <= Paquete(13);
					semaforos.msb(1) <= Paquete(12);
					semaforos.lsb(1) <= Paquete(11);
					semaforos.msb(2) <= Paquete(10);
					semaforos.lsb(2) <= Paquete(9);
					semaforos.msb(3) <= Paquete(8);
					semaforos.lsb(3) <= Paquete(7);
					semaforos.msb(4) <= Paquete(6);
					semaforos.lsb(4) <= Paquete(5);
					semaforos.msb(5) <= Paquete(4);
					semaforos.lsb(5) <= Paquete(3);
					semaforos.msb(6) <= Paquete(2);
					semaforos.lsb(6) <= Paquete(1);
					Cambios <= Paquete(0);
				end if;
			end if;
		end if;
	end process;
end Behavioral;