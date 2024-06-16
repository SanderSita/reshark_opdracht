/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        primary: '#5c6ac4',
        secondary: '#4560ff',
        secondarydark: '#121F2D',
        defaulttext: '#828282',
        grayaccent: '#132436'
      }
    },
  },
  plugins: [],
}

