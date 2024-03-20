/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../templates/*.html",
    "../templates/**/*.html"
  ],
  theme: {
    debugScreens: {
      position: ['bottom', 'right'],
    },
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
    require('tailwindcss-debug-screens')
],
}