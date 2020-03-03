library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity conector_test is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
        switch : in std_logic;
        leds : out std_logic_vector(2-1 downto 0);
        wr_uart : out std_logic;
        w_data_1: in std_logic_vector(8-1 downto 0);
        w_data_2: in std_logic_vector(8-1 downto 0);
        w_data_3: out std_logic_vector(8-1 downto 0)
	);
    end entity;

architecture Behavioral of conector_test is
        
begin
     
    process(clk_i)
    variable count: integer := 0;
    begin
        if (clk_i = '1' and clk_i'event) then
            if switch = '1' then                 
                w_data_3 <= w_data_2; 
                --leds <= "10";
            else                         
                w_data_3 <= w_data_1;
                --leds <= "01";
            end if;
        end if;
    end process;  
    
        
end Behavioral;