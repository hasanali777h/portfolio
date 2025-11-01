const index = () => {
  return (
    <section className="relative hero-section overflow-hidden pt-35 md:pt-40 pb-12 lg:pb-30 xl:pt-52">
      <div className="container">
        <div className="lg:flex grid grid-cols-1 sm:grid-cols-2 gap-7 md:gap-4 items-center">
          <div className="flex flex-col gap-4 md:gap-7 max-w-2xl">
            <div>
              <div className="flex items-center gap-8">
                <h1 className="text-6xl font-semibold">I'm Hasan Anwar</h1>
                <div className="wave">
                </div>
              </div>
              <h1 className="text-6xl font-semibold">Software Engineer</h1>
            </div>
            <p className="text-secondary font-normal max-w-md xl:max-w-xl">
              I am a highly-dedicated, self-motivated and enthusiastic Software Developer that utilizes my expertise in software development.
            </p>
          </div>
        </div>
      </div>
      <div className="absolute right-0 top-0 hidden h-auto w-1/2 lg:block 2xl:h-171.5 2xl:w-187.5">
      </div>
    </section>
  );
};

export default index;
