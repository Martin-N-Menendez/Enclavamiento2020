library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity sum3op is
	generic(
		N: natural := 4
	);
	port(
		a_i: in std_logic_vector(N-1 downto 0);
		b_i: in std_logic_vector(N-1 downto 0);
		c_i: in std_logic_vector(N-1 downto 0);
		s_o: out std_logic_vector(N-1 downto 0)

	);
end;

architecture sum3op_arq of sum3op is
begin
	s_o <= std_logic_vector(unsigned(a_i) + unsigned(b_i) + unsigned(c_i));
end;