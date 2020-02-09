library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;



entity uart_control is
	port(
		clk_i: in std_logic;


		empty_o: in std_logic;
		rd_uart: out std_logic;
		wr_uart: out std_logic
	);
end uart_control;

architecture Behavioral of uart_control is

signal emptySignal: std_logic;
    
begin
    process(clk_i)
        variable count: integer := 0;
    begin
        if rising_edge(clk_i) then
            if empty_o = '0' then
                count := count + 1;
                if count = 100E6 then
                    count := 0;
                    rd_uart <= '1';
                    wr_uart <= '1';
                end if;
            else
                rd_uart <= '0';
                wr_uart <= '0';
            end if;
        end if;
    end process;
    
end Behavioral;
